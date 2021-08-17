import typer
import images_manager

def convert_images_to_pdf(images_path: str, pdf_path: str):
    typer.echo(f"Converting {images_path} to {pdf_path}")
    images_manager.convert_images_to_pdf(images_path, pdf_path)
    typer.echo(f"Conversion complete")



if __name__ == "__main__":
    typer.run(convert_images_to_pdf)