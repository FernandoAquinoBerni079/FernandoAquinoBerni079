Attribute VB_Name = "PasarAOficio"
' ============================================================================
'  PasarAOficio — Edición 2026 Oficio (norma Fer, 02-oct-2026)
'  Oficio 21,59 x 33,02 cm · márgenes 1,27 cm · tablas ajustadas a la ventana
'  · índice actualizado con las páginas reales · sin la leyenda «Ctrl+E / F9».
'  Es la misma migración que hace scripts/formato_oficio.py de la skill, para
'  los tomos que pesan más de 10 MB (7.º, 8.º, 9.º y Economía 2.º).
'
'  USO: abrir el tomo en Word → Alt+F11 → Archivo → Importar archivo →
'  PasarAOficio.bas → cerrar el editor → Alt+F8 → PasarAOficio → Ejecutar.
'  Guarda una copia «..._OFICIO.docx» junto al original; el original no se toca.
' ============================================================================
Option Explicit

Public Sub PasarAOficio()
    Dim doc As Document, s As Section, t As Table, p As Paragraph
    Dim i As Long, n As Long, ruta As String
    Set doc = ActiveDocument
    Application.ScreenUpdating = False

    ' 1. Papel y márgenes en TODAS las secciones
    For Each s In doc.Sections
        With s.PageSetup
            .Orientation = wdOrientPortrait
            .PageWidth = CentimetersToPoints(21.59)
            .PageHeight = CentimetersToPoints(33.02)
            .TopMargin = CentimetersToPoints(1.27)
            .BottomMargin = CentimetersToPoints(1.27)
            .LeftMargin = CentimetersToPoints(1.27)
            .RightMargin = CentimetersToPoints(1.27)
            .HeaderDistance = CentimetersToPoints(1.25)
            .FooterDistance = CentimetersToPoints(1.25)
        End With
    Next s

    ' 2. Tablas de primer nivel a la ventana (100 %, columnas en proporción)
    For Each t In doc.Tables
        t.AllowAutoFit = True
        t.AutoFitBehavior wdAutoFitWindow
        t.PreferredWidthType = wdPreferredWidthPercent
        t.PreferredWidth = 100
        t.Rows.LeftIndent = 0
        n = n + 1
    Next t

    ' 3. Leyenda «presioná Ctrl+E y luego F9»: el índice se entrega poblado
    For i = doc.Paragraphs.Count To 1 Step -1
        Set p = doc.Paragraphs(i)
        If InStr(p.Range.Text, "Ctrl+E") > 0 And InStr(p.Range.Text, "F9") > 0 _
           And Len(p.Range.Text) < 90 Then p.Range.Delete
    Next i

    ' 4. Índice con las páginas reales del oficio
    doc.Repaginate
    For i = 1 To doc.TablesOfContents.Count
        doc.TablesOfContents(i).Update
    Next i
    doc.Fields.Update

    Application.ScreenUpdating = True
    ruta = doc.Path & Application.PathSeparator & _
           Replace(Replace(doc.Name, ".docx", ""), ".DOCX", "") & "_OFICIO.docx"
    doc.SaveAs2 FileName:=ruta, FileFormat:=wdFormatXMLDocument
    MsgBox "Listo: " & n & " tablas ajustadas." & vbCr & _
           "Guardado como: " & ruta & vbCr & vbCr & _
           "Antes de exportar el PDF, recorré el documento buscando páginas" & vbCr & _
           "casi vacías o en blanco (los saltos cambian al pasar de A4 a oficio).", _
           vbInformation, "Edición Oficio"
End Sub
