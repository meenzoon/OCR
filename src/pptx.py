# for local file
import os
from magic_doc.docconv import DocConverter, S3Config
converter = DocConverter(s3_config=None)
markdown_content, time_cost = converter.convert("../file/test.pptx", conv_timeout=300)