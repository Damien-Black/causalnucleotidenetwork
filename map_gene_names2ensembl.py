import sys
from collections import defaultdict

def get_mapping(mapp):
    gmap = defaultdict(set)
    with open(mapp) as f:
        for l in f:
            if len(l.split(",")) != 6:
                print l
                sys.exit()
            # Gene stable ID,Transcript stable ID,HGNC symbol,Chromosome/scaffold name,Gene start (bp),Gene end (bp)
            gene_id, transcript, hgnc, chrom_name, gene_start, gene_end = l.split(",")
            if len(hgnc) > 0:
                if hgnc in gmap and gene_id not in gmap[hgnc]:
                    #print("Multiple hgnc: {}, {}, {}".format(gene_id, gmap[hgnc], hgnc))
                    pass
                gmap[hgnc].add(gene_id)
    return gmap

def map_cancer_genes(cancer_file, gmap):
    cancer_gmap = {}
    with open(cancer_file) as f:
        for l in f:
            if len(l.split()) != 4:
                print l
                sys.exit()
            hgnc, mut, num, freq = l.split() 
            if hgnc in gmap:
                cancer_gmap[hgnc] = gmap[hgnc] 
            else:
                #print hgnc
                pass
    return cancer_gmap


# load data
mapp = sys.argv[1]
kidney = sys.argv[2]
breast = sys.argv[3]

# get one maps for each of the two cancers: {hgnc_name: gene_id}
gmap = get_mapping(mapp)
kmap = map_cancer_genes(kidney, gmap)
bmap = map_cancer_genes(breast, gmap)

#print kmap
for i in kmap.keys():
    if len(kmap[i]) > 1:
        print i, kmap[i]
