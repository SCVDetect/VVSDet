# This file enables data preprocessing, processing, 
# and running Joern to parse functions for obtaining node and edge data.

#!/bin/bash
# cd ..

# Run the first Python script
python3 -B ./sourcescripts/getmetadata.py

# Print a message to the console
echo "All the metadata is being processed"

echo "   ... Starting Joern ..."
# Sleep for 30 seconds
sleep 3

# Run the second Python script
python3 -B ./sourcescripts/getgraphdata.py


# cd ..
cd sourcescripts/storage/outputs/
rm -rf checkpoints
cd ..
cd cache
rm -rf codebert_method_level/
rm -rf Dataset_Vvuldet_codebert_pdg+raw/
rm -rf codebert_method_level/

cd ..
cd ..
cd ..

echo "Ready to train with CVE and CWE descriptions"
echo "   The process takes time. "
echo "The Node2vec should process all functions and generate contextualized graph embedding."
# Sleep for 30 seconds
sleep 3
python3 -B ./sourcescripts/model_cve_cwe.py
