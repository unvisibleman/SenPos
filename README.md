Программа предназначена для вычисления оптимальных координат размещения и типа пожарных извещателей в помещении на гладком потолке в административно-бытовых зданиях.

# Описание логической структуры
Структура программы приведена на рисунке TODO. Взаимодействие с 3D-моделью Revit (получение и сохранение данных, создание экземпляров объектов) реализовано с использованием блоков языка визуального программирования Dynamo. Основная же часть - алгоритм вычисления типа и координат извещателей - написан на языке Python и размещен в блоке «SenPos». Также для упрощения программы, часть кода для решения промежуточных задач написана на языке Python, например:
*	«ParName Remove» удаляет название параметра из вектора, извлеченного из модели;
*	«RemoveNonorth» оставляет в списке извлеченных стен только две ортогональные стены для прямоугольных помещений.

Скрипт Dynamo разделен на 6 основных групп блоков, которые решают изолированные задачи:
*	входные данные,
*	загрузка признака пожара,
*	загрузка и фильтрация стен,
*	загрузка высоты потолка и его типа,
*	вычисление координат,
*	создание экземпляров семейств,
*	генерация отчета.

Пример работы программы приведен на рисунке TODO. В правом нижнем углу расположена вычисленная геометрия: проекции помещений на плоскость, расположенные извещатели.

# Используемые технические средства

Минимальные системные требования:
*	оперативная память 4 Гб для запуска Autodesk Revit и Dynamo;
*	около 5 Гб на накопителей для хранения,
*	операционная система MS Windows 10;
*	Autodesk Revit 2017, Dynamo 2.0.1;
*	минимальные устройства ввода-вывода (монитор и клавиатура).

# Входные данные

Входные данные загружаются из свойств объектов 3D-модели проекта. Основными данными, которые необходимо указать перед использованием программы являются следующие параметры	для объекта «помещение» («Room»):
 *	поле «комментарии» — пожарная нагрузка,
 *	поле «отделка потолка» — тип подвесного потолка.

В среде Dynamo необходимо указать дополнительную информацию:
*	тип системы — адресная или адресно-аналоговая;
*	отметку, в помещениях на которой будут расставлены извещатели.
Пример заполнения свойств помещения и настройки системы приведены на рисунках TODO.

# Выходные данные

В результате работы программа создает в поле 3D-модели проекта экземпляры объектов пожарных извещателей на вычисленных координатах определенного типа.

В качестве справочной информации программа сохраняет в каталоге с проектом файл журнала, содержащий общую информацию о разработанной системе: количество извещателей, их суммарный ток потребления и количество контроллеров (для адресно-аналоговой системы).

Пример выполненной расстановки пожарных извещателей приведен на рисунках TODO.

Пример сгенерированного отчета в формате CSV (comma separated values – значения разделенные запятыми) о расстановке извещателей приведен ниже. Он содержит количество извещателей, суммарный ток потребления в мА, количество контроллеров КДЛ для адресной системы и координаты извещателей в глобальной и локальной (в помещении) системах координат.
```
  Количество извещателей,13
  Ток потребления (мА),6,5
  Количество КДЛ,1
  [17525.0, 25232.0],[1.5, 2.5]
  [13030.0, 24150.0],[3.0, 3.0]
  [7293.0, 24150.0],[3.0, 3.0]
  [11525.0, 16470.0],[1.5, 2.5]
  [6293.0, 16905.0],[2.0, 1.5]
  [6293.0, 13988.0],[2.0, 1.5]
  [6293.0, 10473.0],[2.0, 1.5]
  [11525.0, 10473.0],[1.5, 1.5]
  [14203.0, 10473.0],[1.5, 1.5]
  [25030.0, 10473.0],[3.0, 1.5]
  [25030.0, 13355.0],[3.0, 1.5]
  [25030.0, 16648.0],[3.0, 1.5]
  [25030.0, 19365.0],[3.0, 1.5]
```