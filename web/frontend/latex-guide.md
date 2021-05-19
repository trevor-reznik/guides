
<a name="table-of-contents"/>

![Pictures](banners/latex-guide-banner.png)

---


- [**Templates**](#templates)
	- [Header Templates](#headertemplates)
	- [Math Notes Templates](#mathtemplates)
- [**Math**](#math)
	- [Inline](#inlinemath)
- [**Images**](#images)
	- [Captions](#captions)
	- [In-Text References](#imagereferences)
- [**Highlighting**](#highlighting)



---

![Pictures](banners/latex-guide-banner.png)



<a name="templates"/>

# Templates

 - [Header Templates](#headertemplates)
 - [Math Notes Templates](#mathtemplates)

<a name="headertemplates"/>

#### Headers

```latex
\documentclass{article}
\title{A Small \LaTeX{} Article Template\thanks{To your mother}}
\author{Your Name  \\
    Your Company / University  \\
    \and 
    The Other Dude \\
    His Company / University \\
    }

\begin{document}
\maketitle 

Hello 																																																														

\end{document}
```


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

---


<a name="mathtemplates"/>


#### Math Templates




```latex
\title{Math Notes}
\author{MATH331 - Linear Algebra}

\usepackage{graphicx} 


\usepackage{setspace}


\begin{document}
	
\maketitle
\doublespacing

\section{Continuity}

\begin{description}
	
	\item[1] Piece-Wise Functions 
	
	13 + sin($\pi$/14×7) = 14
	\newline 
	sin($\pi$/2) 
	\newline 
	\emph{Refer to Unit Circle} 
	\newline \begin{math}\frac{\sqrt{3}}{2}\end{math} 
	$>$
	\begin{math}\frac{\sqrt{2}}{2}\end{math} 
	$>$
	\begin{math}\frac{1}{2}\end{math} 
	\newline
	(cos, sin)
	
	
	\item[2] 
	
\end{description}


\end{document}]
```

<a name="math"/>


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

![Pictures](banners/latex-guide-banner.png)



# Math

<a name="inlinemath"/>

###### Inline Math

```latex
inline mode
\begin{math} ... \end{math}.

display mode
\begin{displaymath} ... \end{displaymath}

subscripts
$a_b$

superscripts 
$a^b$

integrals
$\int$

fraction
$\frac{a}{b}$

$\omega$ $\delta$ 
$\Omega$ $\Delta$

math operators
$\sin(\beta)$, $\cos(\alpha)$, $\log(x)$ 
```

<a name="images"/>


<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

![Pictures](banners/latex-guide-banner.png)


# Images

###### Inline 


```latex
\includegraphics{...}
The \includegraphics{universe} command is the one that actually included the image in the document. Here universe is the name of the file containing the image without the extension, then universe.PNG becomes universe. The file name of the image should not contain white spaces nor multiple dots. 
\graphicspath{...}
The command \graphicspath{ {images/} } tells LaTeX that the images are kept in a folder named images under the current directory
```

<a name="captions"/>

###### Captions

```latex
\begin{figure}[h]
	\centering
	\includegraphics[width=0.25\textwidth]{mesh}
	\caption{a nice plot}
	\label{fig:mesh1}
\end{figure}

    \caption{a nice plot}: As you may expect this command sets the caption for the figure. If you create a list of figures this caption will be used there. You can place it above or below the figure.
```

<a name="imagereferences"/>


###### Referencing Images/Figures Throughout Doc


If you need to refer the image within your document, set a label with this command:

```latex
\label{fig:mesh1}: 
````

 The label will number the image, and combined with the next command will allow you to reference it.

Then, 

```latex
\ref{fig:mesh1}: 
```

 will be substituted by the number corresponding to the referenced figure.


<a name="highlighting"/>

<div align="right" font-family="monospace">
    <b><a href="#Highly">↥ Back To Top</a></b>
</div>

![Pictures](banners/latex-guide-banner.png)


# Highlighting

###### Include

```latex
\usepackage{xcolor}

\newcommand{\highlight}[1]{%
  \colorbox{red!50}{$\displaystyle#1$}}
```

###### Enclose Text with Highlight Tag

```latex
\highlight{}
```