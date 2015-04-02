#! /usr/bin/env python
##########################################################################
# NSAp - Copyright (C) CEA, 2013
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

# System import
import os

# CAPSUL import
from capsul.utils.xml_to_pipeline import register_pipelines


# Locate the files containing the pipeline descriptions
xmlpipelines = [
    os.path.join(os.path.dirname(__file__), "spm_new_segment.xml"),
    os.path.join(os.path.dirname(__file__), "spm_smoothing.xml")
]

# Register new pipelines
register_pipelines(xmlpipelines)