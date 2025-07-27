# MedulloblastomaProteomics
Proteomic Biomarker Discovery in Pediatric Medulloblastoma: Identifying Molecular Signatures to Distinguish Tumor Subtypes

### Step 1 - Isoforms
The proteomics data contains protein isoforms - the same gene (symbol) producing multiple protein variants with different functions. Without preprocessing, the expression matrix would have multiple rows with the same gene symbol. This needs to be handled.

<li>
<b>Strategy 1</b>: Assume the most abundant isoform drives biological function and keep the highest expressed isoform. For each gene symbol, keep the row with the highest average expression.
This retains one representative per gene. BUT, might miss important regulatory low abundance isoforms.
</li>

<li>
<b>Strategy 2</b>: Retain maximum biological detail and keep all isoforms with unique names (e.g., "SYNE2_isoform1", "SYNE2_isoform2").
Might find isoform specific biomarkers but analysis more complex and harder to interpret.
</li>

### Step 2 - Grouping
The next task to be handled is grouping. With the Medulloblastoma consensus subgroup from the metadata, we need to split the samples into their respective groups to perform more accurate missingness analysis, imputation and quality control. This will help identify distributions, imbalance and account for differences in the biology across samples from different groups.