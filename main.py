"""
This is a file upload add-on for DocumentCloud.

It demonstrates how to upload a file directly to an add-on.
It then uploads that file to DocumentCloud.
"""

from documentcloud.addon import AddOn


class FileUpload(AddOn):
    """A file upload Add-On for DocumentCloud."""

    def main(self):

        file_id = self.data["file_id"]
        self.set_message(f"File ID {file_id}")
        file_name = self.download_file(file_id)
        self.set_message(f"File name {file_name}")

        self.client.documents.upload(file_name)
        self.set_message(f"{file_name} uploaded")


if __name__ == "__main__":
    FileUpload().main()
