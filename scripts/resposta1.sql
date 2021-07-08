SELECT 
    a.name 'NAME',
    a.email 'EMAIL',
    d.description 'DESCRICAO PAPEL',
    c.description 'DESCRICAO PERMISSOES'    
FROM users              a
LEFT JOIN user_claims   b ON a.id = b.user_id
LEFT JOIN claims        c ON b.claim_id = c.id
LEFT JOIN roles         d ON a.role_id = d.id
WHERE 1 = 1