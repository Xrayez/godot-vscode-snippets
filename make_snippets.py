#!/usr/bin/env python3

'''
Make snippets for Godot C++ development
'''

import re
import os

SNIPPETS_SOURCE_PATH = "src/snippets/"
SNIPPETS_DEST_PATH = "snippets/"

PLACEHOLDER_VARIANT_TYPES = "PLACEHOLDER_VARIANT_TYPES"
PLACEHOLDER_CLASS = "PLACEHOLDER_CLASS"

VARIANT_TYPES = r'''NIL,BOOL,INT,REAL,STRING,VECTOR2,RECT2,VECTOR3,TRANSFORM2D,PLANE,QUAT,AABB,BASIS,TRANSFORM,COLOR,NODE_PATH,_RID,OBJECT,DICTIONARY,ARRAY,POOL_BYTE_ARRAY,POOL_INT_ARRAY,POOL_REAL_ARRAY,POOL_STRING_ARRAY,POOL_VECTOR2_ARRAY,POOL_VECTOR3_ARRAY,POOL_COLOR_ARRAY'''
CLASS = r'''TM_FILENAME_BASE/([A-Za-z0-9]*)_+([A-Za-z0-9]*)/${1:/capitalize}${2:/capitalize}/g'''

def make_snippet():
	# Read snippet source
	with open(SNIPPETS_SOURCE_PATH + 'cpp_raw.json', 'r') as snippet:
		f = snippet.read()

	# Replace template stamps
	f = f.replace(PLACEHOLDER_VARIANT_TYPES, VARIANT_TYPES)
	f = f.replace(PLACEHOLDER_CLASS, CLASS)

	# Write snippet source
	with open(SNIPPETS_DEST_PATH + 'cpp.json', 'w') as snippet:
		snippet.write(f)

if __name__ == "__main__":
	make_snippet()
