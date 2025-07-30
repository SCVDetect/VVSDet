### Domain-Aware Graph Neural Networks for Source Code Vulnerability Detection
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



### Results
## Data Contents

Below is a preview of the contents of :

| CWE_ID   | num_functions | num_statements | func_accuracy | func_precision | func_recall | func_f1 | func_mcc | stmt_accuracy | stmt_precision | stmt_recall | stmt_f1 | stmt_mcc | func_pr_auc | stmt_pr_auc |
|----------|---------------|----------------|---------------|----------------|-------------|---------|----------|---------------|----------------|-------------|---------|----------|--------------|--------------|
| CWE-502  | 123           | 1062           | 1             | 1              | 1           | 1       | 1        | 0.985875706   | 0.494334278    | 0.498571429 | 0.496443812 | -0.005689952 | 1            | 0.021936825  |
| CWE-732  | 22            | 324            | 1             | 1              | 1           | 1       | 1        | 0.987654321   | 0.49382716     | 0.5         | 0.49689441  | 0            | 1            | 0.051721866  |
| CWE-284  | 114           | 1283           | 0.99122807    | 0.75           | 0.995575221 | 0.831111111 | 0.703971037 | 0.998441154   | 0.499609984    | 0.499609984 | 0.499609984 | -0.000780031 | 0.25         | 0.03125      |
| CWE-863  | 207           | 1728           | 0.995169082   | 0.75           | 0.997572816 | 0.832116788 | 0.705388415 | 0.996527778   | 0.499130435    | 0.499130435 | 0.499130435 | -0.00173913  | 0.25         | 0.276984127  |
| CWE-20   | 183           | 1531           | 0.983606557   | 0.8125         | 0.991573034 | 0.880366093 | 0.783879004 | 0.988896146   | 0.497371879    | 0.497045305 | 0.497208539 | -0.005573256 | 0.406785714  | 0.046173182  |


### Citation

To be provided


##### Acknowledgment:
###### We thank [LineVD](https://github.com/davidhin/linevd) for providing the source code of their project, which has served as a foundation for the current research project.
