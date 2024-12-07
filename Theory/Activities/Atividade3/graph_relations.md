```mermaid
graph TB;
  %% Pessoas
  subgraph Familia
    direction LR
    MatheusFonseca["Matheus Fonseca<br>Engenheiro<br>Idade: 21"]
    JuliaFonseca["Julia Fonseca<br>Estudante<br>Idade: 17"]
    CharlenyFonseca["Charleny Fonseca<br>Polvilheira<br>Idade: 40"] -->|Mãe de| MatheusFonseca
    CharlenyFonseca -->|Mãe de| JuliaFonseca

    ZeGalinha["Zé Galinha<br>Polvilheiro<br>Idade: 65"] -->|Pai de| CharlenyFonseca
    ZeGalinha -->|Pai de| PauloFonseca["Paulo Fonseca<br>Caminhoneiro<br>Idade: 39"]
    ZeGalinha -->|Pai de| ElismaraFonseca["Elismara Fonseca<br>Vendedora<br>Idade: 42"]

    Cida["Cida<br>Professora<br>Idade: 66"] -->|Mãe de| CharlenyFonseca
    Cida -->|Mãe de| PauloFonseca
    Cida -->|Mãe de| ElismaraFonseca

    MatheusFonseca ---|Irmão de<br>Irmão mais velho de| JuliaFonseca
  end

    direction LR
    PauloFonseca ---|Tio de| MatheusFonseca
    PauloFonseca ---|Tio de| JuliaFonseca

    ElismaraFonseca ---|Tia de| MatheusFonseca
    ElismaraFonseca ---|Tia de| JuliaFonseca

    CharlenyFonseca ---|Irmã de| PauloFonseca
    CharlenyFonseca ---|Irmã de| ElismaraFonseca

    PauloFonseca ---|Irmão de| ElismaraFonseca
    PauloFonseca ---|Irmão de| CharlenyFonseca

    ElismaraFonseca ---|Irmã de<br>Irmã mais velho de| PauloFonseca
    ElismaraFonseca ---|Irmã de<br>Irmã mais velho de| CharlenyFonseca

    ZeGalinha ---|Casado com<br>desde 1980| Cida
    Cida ---|Casado com<br>desde 1980| ZeGalinha

  %% Animais
  subgraph Animais
    direction LR
    Zeus["Zeus<br>Cachorro<br>Raça: Lhasa Apso<br>Idade: 6"] 
    Lua["Lua<br>Cachorro<br>Raça: Red Heeler<br>Idade: 14"]
    Estrela["Estrela<br>Gato<br>Raça: Ragdoll<br>Idade: 3"]
  end

  %% Relações com Animais
  JuliaFonseca ---|Dona de<br>desde 2018<br>Apelido: Gordinho| Zeus;
  PauloFonseca ---|Dono de<br>desde 2010<br>Apelido: Sem Vergonha| Lua;
  ElismaraFonseca ---|Dona de| Estrela;
```