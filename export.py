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
