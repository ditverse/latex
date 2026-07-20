#!/usr/bin/env python3
"""
PDF to Markdown Extractor
Extracts text content from all PDFs in references/ folder
and saves as markdown files in references/extraction/
"""

import os
import pymupdf  # PyMuPDF
from pathlib import Path

def extract_pdf_to_markdown(pdf_path, output_path):
    """Extract text from PDF and save as markdown"""
    doc = None
    try:
        # Open PDF with absolute path
        pdf_path_str = str(pdf_path.absolute())
        doc = pymupdf.open(pdf_path_str)
        
        # Check if document is valid
        if doc is None or doc.is_closed:
            return False, "Failed to open document"
        
        page_count = doc.page_count
        
        # Prepare markdown content
        markdown_content = []
        
        # Add header with metadata
        pdf_name = os.path.basename(pdf_path)
        markdown_content.append(f"# Extracted from: {pdf_name}\n")
        markdown_content.append(f"**Total Pages**: {page_count}\n")
        markdown_content.append(f"**Extraction Date**: 2026-07-20\n")
        markdown_content.append("\n---\n\n")
        
        # Extract text from each page
        for page_num in range(page_count):
            page = doc.load_page(page_num)
            text = page.get_text()
            
            if text.strip():  # Only add non-empty pages
                markdown_content.append(f"## Page {page_num + 1}\n\n")
                markdown_content.append(text)
                markdown_content.append("\n\n---\n\n")
        
        # Write to markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(markdown_content))
        
        return True, page_count
        
    except Exception as e:
        import traceback
        error_details = f"{type(e).__name__}: {str(e)}"
        return False, error_details
    finally:
        if doc is not None and not doc.is_closed:
            doc.close()

def main():
    """Main extraction function"""
    # Set paths
    references_dir = Path("references")
    extraction_dir = references_dir / "extraction"
    
    # Ensure extraction directory exists
    extraction_dir.mkdir(exist_ok=True)
    
    # Find all PDF files
    pdf_files = list(references_dir.glob("*.pdf"))
    
    print(f"Found {len(pdf_files)} PDF files to extract\n")
    print("=" * 60)
    
    success_count = 0
    failed_count = 0
    
    # Process each PDF
    for pdf_path in pdf_files:
        pdf_name = pdf_path.name
        output_name = pdf_path.stem + ".md"
        output_path = extraction_dir / output_name
        
        print(f"\nExtracting: {pdf_name}")
        
        success, result = extract_pdf_to_markdown(pdf_path, output_path)
        
        if success:
            print(f"  [OK] Success - {result} pages extracted")
            print(f"  --> Saved to: extraction/{output_name}")
            success_count += 1
        else:
            print(f"  [FAIL] Failed: {result}")
            failed_count += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"\nExtraction Summary:")
    print(f"  Success: {success_count} files")
    print(f"  Failed:  {failed_count} files")
    print(f"  Total:   {len(pdf_files)} files")
    print(f"\nAll extracted files saved to: {extraction_dir}")

if __name__ == "__main__":
    main()
