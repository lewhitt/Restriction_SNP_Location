##This file runs CdRestrictionSiteLocator.py and SNP_RestrictionMatching.py
##for every restriction enzyme in the list. Make sure the seqs match the
##name of their corresponding enzyme.

enzymes=("bamHI" "ecoRI" "hindIII" "pstl" "pvull" "xhol")
seqs=("GGATCC" "GAATTC" "AAGCTT" "CTGCAG" "CAGCTG" "CTCGAG")
arrLen=${#enzymes[@]}

for ((i=0; i<${arrLen}; i++)); 
do
    python CdRestrictionSiteLocator.py -r ${seqs[$i]} -o ${enzymes[$i]}
done

regions=()
for f in `find . -type f -name '*_regions' -printf "%f\n"`; 
do 
    regions+=($f)
done

regions=($(for l in ${regions[@]}; do echo $l; done | sort))
echo ${regions[@]}

for ((q=0; q<${arrLen}; q++));
do
    python SNP_RestrictionMatching.py -r ${regions[$q]} -s coordSNP.txt -o ${enzymes[$q]}
done

