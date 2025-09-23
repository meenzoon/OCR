# for local file
from magic_doc.docconv import DocConverter, S3Config
converter = DocConverter(s3_config=None)
markdown_content, time_cost = converter.convert("../file/hadoop-설명자료.pptx", conv_timeout=300)