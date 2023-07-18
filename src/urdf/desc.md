link的子标签列表

visual 显示形状
<geometry> (几何形状)
<box> 长方体
标签属性: size-长宽高
举例：<box size="1 1 1" />
<cylinder> 圆柱体
标签属性:radius -半径 length-高度
举例：<cylinder radius="1" length="0.5"/>
sphere 球体
属性：radius -半径
举例：<sphere radius="0.015"/>
mesh 第三方导出的模型文件
属性：filename
举例: <mesh filename="package://robot_description/meshes/base_link.DAE"/>
origin (可选：默认在物体几何中心)
属性 xyz默认为零矢量 rpy弧度表示的翻滚、俯仰、偏航
举例：<origin xyz="0 0 0" rpy="0 0 0" />
material 材质
属性 name 名字
color
属性 rgba a代表透明度
举例：<material name="white"><color rgba="1.0 1.0 1.0 0.5" /> </material>
collision 碰撞属性，仿真章节中讲解
inertial 惯性参数 质量等，仿真章节中讲解


joint标签详解
joint属性
name 关节的名称
type 关节的类型
revolute: 旋转关节，绕单轴旋转,角度有上下限,比如舵机0-180
continuous: 旋转关节，可以绕单轴无限旋转,比如自行车的前后轮
fixed: 固定关节，不允许运动的特殊关节
prismatic: 滑动关节，沿某一轴线移动的关节，有位置极限
planer: 平面关节，允许在xyz，rxryrz六个方向运动
floating: 浮动关节，允许进行平移、旋转运动

joint的子标签
parent 父link名称
 <parent link="base_link" />
child子link名称
<child link="laser_link" />
origin 父子之间的关系xyz rpy
 <origin xyz="0 0 0.014" />
axis 围绕旋转的关节轴
<axis xyz="0 0 1" />