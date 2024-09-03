for proc_count in 512 1024 ; do
    PYTHONPATH=. ./bin/calculon llm-optimal-execution models/megatron-1T.json $proc_count 256 float16 systems/testsystem.json results/diff_tech_analysis/output_imec_${proc_count}_256.csv -m
done