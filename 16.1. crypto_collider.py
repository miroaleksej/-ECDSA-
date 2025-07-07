def crypto_collider(key1, key2, curve):
    """Столкновение топологии двух ключей"""
    fp1 = TopologicalKeyFingerprint(key1, curve).compute_topological_features()
    fp2 = TopologicalKeyFingerprint(key2, curve).compute_topological_features()

    # Метрика "топологического сечения"
    cross_section = 0
    for k in ['edge_mean', 'rx_entropy', 'curvature_mean']:
        cross_section += (fp1[k] - fp2[k]) ** 2

    # Детектирование сингулярностей
    anomalies = []
    if cross_section > 1.0:  # Порог срабатывания
        anomalies.append({
            'type': 'topological_detect',  # Исправлено defect → detect
            'position': (key1, key2),
            'energy': cross_section
        })
    
    return {
        'anomalies': anomalies,
        'cross_section': cross_section
    }

# Пример использования
if __name__ == "__main__":
    result = crypto_collider(
        key1=0x2a9d3d7e45f8c1a0b,
        key2=0x3b8c9d0e1f2a3b4c,
        curve="P256"
    )
    
    if result['anomalies']:
        anomaly_type = result['anomalies'][0]['type']
        print(f"Обнаружена уязвимость типа '{anomaly_type}'! Энергия: {result['anomalies'][0]['energy']:.2f}")
    else:
        print("Аномалии не обнаружены")