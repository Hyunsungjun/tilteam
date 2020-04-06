# PDF 파일 다운로드 기능

```
public FileResult Download()
    {
        string fileName = "사용자가_다운받을_파일명.pdf";
        string filePath = Server.MapPath(Path.Combine("실제_파일_경로", "실제_파일명.pdf"));

        byte[] fileBytes = System.IO.File.ReadAllBytes(filePath);

        return File(fileBytes, System.Net.Mime.MediaTypeNames.Application.Pdf, fileName);
    }
```