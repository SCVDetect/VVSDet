## Domain-Aware Graph Neural Networks for Source Code Vulnerability Detection
Paper submitted to XXX Journal.

### Section 1: Experiment Replication

The source code for training the model is located in `./sourcescripts`, and the dataset construction instructions can be found in `./domainknowledge`.

1. **Clone the project repository.**

```bash
   git clone https://github.com/RosmaelZidane/VVulDet.git
```

2. **Install the required Python packages.**

```bash
pip install -r requirements.txt
```
3. **Dataset and CPG Extraction.**

Dataset: We used publicly available datasets named BigVul-C/C++, Project_KB-Java, MegaVul-Java, and CVEFixes-Python.

CPG Extraction: We use Joern to parse the source code, extracting relevant nodes and edge data.

Running the following commands will install a specific Joern version for CPG extraction and download the Python version of the CVEFixes dataset from our drive.

```bash
chmod +x ./run.sh
./run.sh
./zrun/getjoern.sh
```

4. **Train/Test.**

```bash
./zrun/Process_train_test.sh
```

The results will be stored in ```storage/outputs/```.



### Section 2: **Gathering Domain Data.**

Navigate to ```./domainknowledge```.




### Citation

To be provided


##### Acknowledgment:
###### We thank [LineVD](https://github.com/davidhin/linevd) for providing the source code of their project, which has served as a foundation for the current research project.
