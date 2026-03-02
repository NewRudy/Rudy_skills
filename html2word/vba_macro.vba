Sub ConvertLatexToMath()
    ' ============================================
    ' html2word VBA Macro - LaTeX to Word Math
    ' Version: 1.0.0
    ' Author: Claude (Claudian)
    ' Date: 2026-02-02
    ' ============================================
    ' Converts LaTeX formulas ($...$) and ($$...$$) to Word equations
    ' Automatically replaces Greek letters and common symbols
    ' ============================================

    Dim doc As Document
    Dim rng As Range
    Dim strFormula As String

    Set doc = ActiveDocument
    Application.ScreenUpdating = False

    ' ========== Step 1: Process Display Formulas ($$...$$) ==========
    Set rng = doc.Content
    With rng.Find
        .ClearFormatting
        .Text = "\$\$([!$]@)\$\$"
        .MatchWildcards = True
        .Wrap = wdFindContinue

        Do While .Execute
            strFormula = Mid(rng.Text, 3, Len(rng.Text) - 4)
            strFormula = ReplaceGreekLetters(strFormula)
            rng.Text = strFormula
            rng.OMaths.Add rng
            rng.OMaths(1).BuildUp
            rng.Collapse wdCollapseEnd
        Loop
    End With

    ' ========== Step 2: Process Inline Formulas ($...$) ==========
    Set rng = doc.Content
    With rng.Find
        .ClearFormatting
        .Text = "\$([!$]@)\$"
        .MatchWildcards = True
        .Wrap = wdFindContinue

        Do While .Execute
            strFormula = Mid(rng.Text, 2, Len(rng.Text) - 2)
            strFormula = ReplaceGreekLetters(strFormula)
            rng.Text = strFormula
            rng.OMaths.Add rng
            rng.OMaths(1).BuildUp
            rng.Collapse wdCollapseEnd
        Loop
    End With

    Application.ScreenUpdating = True
    MsgBox "公式转换完成！共处理 " & doc.OMaths.Count & " 个公式。", vbInformation, "html2word"
End Sub

Function ReplaceGreekLetters(ByVal formula As String) As String
    ' ========== Greek Letters (Lowercase) ==========
    formula = Replace(formula, "\alpha", "α")
    formula = Replace(formula, "\beta", "β")
    formula = Replace(formula, "\gamma", "γ")
    formula = Replace(formula, "\delta", "δ")
    formula = Replace(formula, "\epsilon", "ε")
    formula = Replace(formula, "\varepsilon", "ϵ")
    formula = Replace(formula, "\zeta", "ζ")
    formula = Replace(formula, "\eta", "η")
    formula = Replace(formula, "\theta", "θ")
    formula = Replace(formula, "\vartheta", "ϑ")
    formula = Replace(formula, "\iota", "ι")
    formula = Replace(formula, "\kappa", "κ")
    formula = Replace(formula, "\lambda", "λ")
    formula = Replace(formula, "\mu", "μ")
    formula = Replace(formula, "\nu", "ν")
    formula = Replace(formula, "\xi", "ξ")
    formula = Replace(formula, "\pi", "π")
    formula = Replace(formula, "\varpi", "ϖ")
    formula = Replace(formula, "\rho", "ρ")
    formula = Replace(formula, "\varrho", "ϱ")
    formula = Replace(formula, "\sigma", "σ")
    formula = Replace(formula, "\varsigma", "ς")
    formula = Replace(formula, "\tau", "τ")
    formula = Replace(formula, "\upsilon", "υ")
    formula = Replace(formula, "\phi", "φ")
    formula = Replace(formula, "\varphi", "ϕ")
    formula = Replace(formula, "\chi", "χ")
    formula = Replace(formula, "\psi", "ψ")
    formula = Replace(formula, "\omega", "ω")

    ' ========== Greek Letters (Uppercase) ==========
    formula = Replace(formula, "\Gamma", "Γ")
    formula = Replace(formula, "\Delta", "Δ")
    formula = Replace(formula, "\Theta", "Θ")
    formula = Replace(formula, "\Lambda", "Λ")
    formula = Replace(formula, "\Xi", "Ξ")
    formula = Replace(formula, "\Pi", "Π")
    formula = Replace(formula, "\Sigma", "Σ")
    formula = Replace(formula, "\Upsilon", "Υ")
    formula = Replace(formula, "\Phi", "Φ")
    formula = Replace(formula, "\Psi", "Ψ")
    formula = Replace(formula, "\Omega", "Ω")

    ' ========== Binary Operators ==========
    formula = Replace(formula, "\pm", "±")
    formula = Replace(formula, "\mp", "∓")
    formula = Replace(formula, "\times", "×")
    formula = Replace(formula, "\div", "÷")
    formula = Replace(formula, "\cdot", "·")
    formula = Replace(formula, "\ast", "∗")
    formula = Replace(formula, "\star", "⋆")
    formula = Replace(formula, "\circ", "∘")
    formula = Replace(formula, "\bullet", "•")
    formula = Replace(formula, "\oplus", "⊕")
    formula = Replace(formula, "\ominus", "⊖")
    formula = Replace(formula, "\otimes", "⊗")
    formula = Replace(formula, "\oslash", "⊘")
    formula = Replace(formula, "\odot", "⊙")

    ' ========== Relation Symbols ==========
    formula = Replace(formula, "\neq", "≠")
    formula = Replace(formula, "\ne", "≠")
    formula = Replace(formula, "\leq", "≤")
    formula = Replace(formula, "\le", "≤")
    formula = Replace(formula, "\geq", "≥")
    formula = Replace(formula, "\ge", "≥")
    formula = Replace(formula, "\approx", "≈")
    formula = Replace(formula, "\equiv", "≡")
    formula = Replace(formula, "\sim", "∼")
    formula = Replace(formula, "\simeq", "≃")
    formula = Replace(formula, "\cong", "≅")
    formula = Replace(formula, "\propto", "∝")
    formula = Replace(formula, "\ll", "≪")
    formula = Replace(formula, "\gg", "≫")
    formula = Replace(formula, "\in", "∈")
    formula = Replace(formula, "\notin", "∉")
    formula = Replace(formula, "\subset", "⊂")
    formula = Replace(formula, "\supset", "⊃")
    formula = Replace(formula, "\subseteq", "⊆")
    formula = Replace(formula, "\supseteq", "⊇")

    ' ========== Arrows ==========
    formula = Replace(formula, "\rightarrow", "→")
    formula = Replace(formula, "\to", "→")
    formula = Replace(formula, "\leftarrow", "←")
    formula = Replace(formula, "\gets", "←")
    formula = Replace(formula, "\Rightarrow", "⇒")
    formula = Replace(formula, "\Leftarrow", "⇐")
    formula = Replace(formula, "\leftrightarrow", "↔")
    formula = Replace(formula, "\Leftrightarrow", "⇔")
    formula = Replace(formula, "\uparrow", "↑")
    formula = Replace(formula, "\downarrow", "↓")
    formula = Replace(formula, "\Uparrow", "⇑")
    formula = Replace(formula, "\Downarrow", "⇓")

    ' ========== Miscellaneous Symbols ==========
    formula = Replace(formula, "\infty", "∞")
    formula = Replace(formula, "\nabla", "∇")
    formula = Replace(formula, "\partial", "∂")
    formula = Replace(formula, "\hbar", "ℏ")
    formula = Replace(formula, "\ell", "ℓ")
    formula = Replace(formula, "\emptyset", "∅")
    formula = Replace(formula, "\exists", "∃")
    formula = Replace(formula, "\nexists", "∄")
    formula = Replace(formula, "\forall", "∀")
    formula = Replace(formula, "\neg", "¬")
    formula = Replace(formula, "\wedge", "∧")
    formula = Replace(formula, "\vee", "∨")
    formula = Replace(formula, "\cap", "∩")
    formula = Replace(formula, "\cup", "∪")
    formula = Replace(formula, "\int", "∫")
    formula = Replace(formula, "\iint", "∬")
    formula = Replace(formula, "\iiint", "∭")
    formula = Replace(formula, "\oint", "∮")
    formula = Replace(formula, "\sum", "∑")
    formula = Replace(formula, "\prod", "∏")
    formula = Replace(formula, "\coprod", "∐")
    formula = Replace(formula, "\angle", "∠")
    formula = Replace(formula, "\perp", "⊥")
    formula = Replace(formula, "\parallel", "∥")
    formula = Replace(formula, "\therefore", "∴")
    formula = Replace(formula, "\because", "∵")

    ReplaceGreekLetters = formula
End Function
