#!/bin/bash
cd ../deeplearnjs
python scripts/dump_checkpoints/dump_checkpoint_vars.py \
--model_type=tensorflow --output_dir=../game-of-life/deeplearnjs_model \
--checkpoint_file=../game-of-life/tensorflow_model/model.ckpt-6000
cd -