### TkInter

TkInter é uma junção das palavras Tk (biblioteca padrão) e Interface.

Ela é uma biblioteca nativa do python e também é multiplataforma.

### Definições:

**widget**: 
Um componente, ou seja, qualquer parte da interface gráfica.
Ex: frame, label, botão, botões de opções, campos de texto, janelas, rótulos de texto, etc...

**Container**:
Um _widget_ que pode conter outros _widgets_. Ou seja, alguma parte gráfica que contém vários conteúdos.
Ex: janela

**Window**:
Uma janela propriamente dita.
Ex: uma janela retangular capaz de receber outros componentes

**top-leve window**:
Janela independente que está sobrescrita nas demais.
Ex: abrir uma janela que abre outra janela para coletar informações; ou tomar determinadas decisões.

**frame**:
Uma unidade básica da organização de layouts complexos.

**child-parent**:
Nome que se dá pela relação entre um widget e seu container.
Obs: todo widget é criado dentro de um container, logo devemos realizar a relação entre eles.

**Gerenciador de layout**
Define a organização das widgets dentro de um container.
    - place: definindo coordenadas x e y
    - pack: empacota widgets em x e y
    - grid: distribuir em linhas e colunas (nas celulas definidas)

_**Toda janela é um container que pode conter outros widgets presente em um window.**_

#### Observação:
Posso usar a palavra GUI algumas vezes que significa:
```
G raphic
U ser
I nterface
```
Ou seja, interface gráfica do usuário.