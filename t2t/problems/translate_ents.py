
# coding=utf-8
# Copyright 2018 The Tensor2Tensor Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Data generators for translation data-sets."""

import os
from tensor2tensor.data_generators import generator_utils
from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_encoder
from tensor2tensor.data_generators import text_problems
from tensor2tensor.data_generators import translate
from tensor2tensor.utils import registry

import tensorflow as tf

EOS = text_encoder.EOS_ID


_ENTS_TRAIN_DATASETS = [
    [
        "https://github.com/LauraMartinus/ukuxhumana/blob/master/clean/en_ts/en_ts.train.tar.gz?raw=true",
        (
            "ents_parallel.train.en",
            "ents_parallel.train.ts"
        )
    ]
]

_ENTS_TEST_DATASETS = [
    [
        "https://github.com/LauraMartinus/ukuxhumana/blob/master/clean/en_ts/en_ts.dev.tar.gz?raw=true",
        (
            "ents_parallel.dev.en",
            "ents_parallel.dev.ts"
        )
    ]
]


@registry.register_problem
class TranslateEntsRma(translate.TranslateProblem):
  """Problem spec for English-Xitsonga translation."""

  @property
  def approx_vocab_size(self):
    return 2**15  # 32768

  @property
  def vocab_filename(self):
    return "vocab.ents.%d" % self.approx_vocab_size


  def source_data_files(self, dataset_split):
    train = dataset_split == problem.DatasetSplit.TRAIN
    return _ENTS_TRAIN_DATASETS if train else _ENTS_TEST_DATASETS