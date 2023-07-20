from Bio import SeqIO
import xml.etree.ElementTree as ET
from xml.dom import minidom

# This script automates the extraction of information from a Genbank file to an XML file

# Open the GenBank file
input_genbank_file = "./src/sequence.gb"

# List to store the processed sequences
sequences_data = []

# Read strings from the GenBank file and extract the desired information
for record in SeqIO.parse(input_genbank_file, "genbank"):
    sequence_data = {
        "TSeq_seqtype": {"value": "nucleotide"},
        "TSeq_accver": record.id,
        "TSeq_taxid": "",  # Initially empty
        "TSeq_orgname": record.annotations.get("organism", ""),
        "TSeq_voucher": [],  # Initially empty
        "TSeq_country": "",  
        "TSeq_collection_date": "",  # Initially empty
        "TSeq_collected_by": "",  # Initially empty
        "TSeq_identified_by": "",  # Initially empty
        "TSeq_title": "",  # Initially empty
        "TSeq_authors": "",  # Initially empty
        "TSeq_journal": "",  # Initially empty
        "TSeq_defline": record.description,
        "TSeq_length": str(len(record.seq)),
        "TSeq_sequence": str(record.seq),
    }

    if references := record.annotations.get("references", []):
        sequence_data["TSeq_title"] = references[0].title
        sequence_data["TSeq_journal"] = references[0].journal
        sequence_data["TSeq_authors"] = ", ".join(ref.authors for ref in references)

    # Extracting taxon information
    for feature in record.features:
        qualifiers = feature.qualifiers
        if feature.type == "source":
            if "specimen_voucher" in qualifiers:
                sequence_data["TSeq_voucher"].append((qualifiers["specimen_voucher"][0]))
            if "country" in qualifiers:
                sequence_data["TSeq_country"] = qualifiers["country"][0]
            if "collection_date" in qualifiers:
                sequence_data["TSeq_collection_date"] = qualifiers["collection_date"][0]
            if "collected_by" in qualifiers:
                sequence_data["TSeq_collected_by"] = qualifiers["collected_by"][0]
            if "identified_by" in qualifiers:
                sequence_data["TSeq_identified_by"] = qualifiers["identified_by"][0]
            if "db_xref" in qualifiers:
                for dbxref in qualifiers["db_xref"]:
                    if dbxref.startswith("taxon:"):
                        sequence_data["TSeq_taxid"] = dbxref.split(":")[1]

    sequences_data.append(sequence_data)


# XML file creation
root = ET.Element("TSeqSet")

for sequence_data in sequences_data:
    tseq = ET.SubElement(root, "TSeq")

    # Adds the columns to the XML using the order they were entered in sequence_data
    for key, value in sequence_data.items():
        tseq_element = ET.SubElement(tseq, key)
        if key == "TSeq_voucher":
            for voucher_value in value:
                tseq_voucher = ET.SubElement(tseq, key)
                tseq_voucher.text = voucher_value
        elif isinstance(value, dict):
            tseq_element.set("value", value["value"])
        else:
            tseq_element.text = value

# Turns the XML into a formatted string
xml_string = ET.tostring(root, encoding="utf-8")
pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")

# Save the content in the XML file
output_xml_file = "output0.xml"
with open(output_xml_file, "w") as xml_output:
    xml_output.write(pretty_xml)

print(f"Your database in XML format has been successfully created: {output_xml_file}")