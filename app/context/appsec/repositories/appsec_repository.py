
class AppsecRepository:
    async def get_practice(self, key: str):
        if key == "practice_main":
                return practice
        else:
            return {'practice': practice[key]}



practice = {
    'sast': 'SAST (Static Application Security Testing) – это один из методов тестирования защищенности приложений. Статический анализ кода приложения/программы или его части на наличие уязвимостей реализуется без реального запуска исследуемого приложения в «боевой среде». А SAST-анализатор реализует этот подход. Такую технологию еще принято называть тестированием по методу белого ящика.',
    'sca': 'SCA (Software composition analysis) — это методика, основанная на сканировании и анализе компонентов с открытым исходным кодом на наличие известных уязвимостей. Она помогает компаниям обеспечивать безопасность приложений и предотвращать атаки, реализуемые за счёт наличия проблемных компонентов. Компонентный анализ, как правило, выполняет следующие действия: проверяет код сторонних разработчиков; находит известные уязвимости; выявляет проблемы с лицензиями; обнаруживает вредоносные программы; ищет случаи модификации кода; выделяет слабые шаблоны кода.',
    'dast': 'DAST (Dynamic Application Security Testing) – это процесс тестирования приложений, имитирующий вредоносные внешние атаки, пытающиеся использовать распространенные уязвимости. Главная задача DAST – обнаружение уязвимостей до того, как их обнаружит кто-то, кроме разработчиков.',
    'iast': 'IAST (Interactive Application Security Testing) – это относительно новый (в сравнении, опять же, с SAST и DAST) тип тестирования приложений, который фокусируется на обнаружении проблем безопасности в коде приложений. Технология интерактивного тестирования позволяет анализировать приложение изнутри во время его работы.',
    'rasp': 'RASP (Run-time Application Security Protection) — защита безопасности приложений во время выполнения. Как и IAST работает внутри приложения, но это скорее инструмент безопасности, а не тестирования. Он подключается к приложению или его среде выполнения и может контролировать выполнение приложения. Это позволяет RASP защитить приложение, даже если защита периметра сети нарушена, а приложения содержат уязвимости безопасности.',
}