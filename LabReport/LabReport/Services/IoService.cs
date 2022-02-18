using LabReport.Tools;

namespace LabReport.Services;

public class IoService
{
    public string GetPathFolder()
    {
        Console.Write("Input path folder: ");

        string path = Console.ReadLine();
        if (!Directory.Exists(path))
            throw new LabReportException("folder with that path does not exist");

        return path;
    }

    public bool GetDoBackup()
    {
        Console.Write("Do backup (y/n): ");
        return Console.ReadLine() switch
        {
            "y" or "Y" => true,
            "n" or "N" => false,
            _ => throw new LabReportException("incorrect backup info input")
        };
    }

    public void PrintError(string message) =>
        Console.WriteLine($"Error: {message}");
}