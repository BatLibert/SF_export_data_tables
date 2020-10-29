<h1 align="center">👋 on Spotfire IronPython export</h1>

## ✨ Demo
<p align="center"><img src="http://dataviz-ressources.com/wp-content/uploads/2017/04/Spotfire-Export-GIF-2.gif" /></p>

## 📚 Prerequisites
- Spotfire Desktop

## ⚙️ Install
> Note this tool will allow you to:
* Export any data table on the report as data visualization. It means, if you decide to limite the data and/or to show only some columns of the data table, the file will be export as it.
* Choose the export folder on your computer by a document property (« C:\\ »…)
* Customize the name of the export file by a document property (« _2017 », « _ByMe »…)

`IronPython Code`

    from System.IO import Path, File, StreamWriter
    from Spotfire.Dxp.Application.Visuals import TablePlot
    from System.IO import Path, File, StreamWriter
    from Spotfire.Dxp.Application.Visuals import TablePlot
    from Spotfire.Dxp.Data import DataPropertyClass
    from Spotfire.Dxp.Data import DataType
    
    for d in Document.Data.Properties.GetProperties(0):
     if d.IsUserVisible and d.Name == "ReportingDate": x = d.Value

    for f in Document.Data.Properties.GetProperties(0):
     if f.IsUserVisible and f.Name == "ReportingFolder": y = f.Value

    tempFilename = y + "\\sp500overview_" + x + ".csv"
    writer = StreamWriter(tempFilename)
    Viz1.As[TablePlot]().ExportText(writer)

    tempFilename = y + "\\sp500price_" + x + ".csv"
    writer = StreamWriter(tempFilename)
    Viz2.As[TablePlot]().ExportText(writer)

    tempFilename = y + "\\sp500marketvalue_" + x + ".csv"
    writer = StreamWriter(tempFilename)
    Viz3.As[TablePlot]().ExportText(writer)

> You must pay attention to select your input for the selected script as below (« Viz1 », « Viz2 » and « Viz3 »).

The objective is to give to each export the data visualization concerned : Viz3.As[TablePlot] is concerning the Viz3 selected as input. Then, as you can see on the script above, x and y are defined as the ReportingDate and ReportingFolder’ document properties. Both can be modify directly in the analysis by input fields (HTML).

<p align="center"><img src="http://dataviz-ressources.com/wp-content/uploads/2017/04/Spotfire-Export-Tuto.png" /></p>

## 👤 Author
<table>
  <tr>
    <td align="center">
    	<a href="https://github.axa.com/baptiste-libert">
    	<img src="https://avatars0.githubusercontent.com/u/24935223?s=460&u=b6e484f9d4593131a7b5d57c474f3e27e55c3145&v=4" height="80" width="80"/><br />
    	Bat</a>
    </td>
  </tr>
</table>
  
## Show your support
Give a ⭐️ if this project helped you. Contributions, issues and feature requests are welcome!


<a href="https://www.buymeacoffee.com/batlib"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=batlib&button_colour=5F7FFF&font_colour=ffffff&font_family=Poppins&outline_colour=000000&coffee_colour=FFDD00"></a>***
