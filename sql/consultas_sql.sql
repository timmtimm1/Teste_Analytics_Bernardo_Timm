-- 1. Total de vendas por produto e categoria
SELECT 
    Produto,
    Categoria,
    ROUND(SUM(Quantidade * Preco), 2) as Total_Vendas
FROM vendas
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;

-- 2. Produtos com menores vendas em junho
SELECT 
    Produto,
    ROUND(SUM(Quantidade * Preco), 2) as Total_Vendas
FROM vendas
WHERE strftime('%m', Data) = '06'
GROUP BY Produto
ORDER BY Total_Vendas ASC;