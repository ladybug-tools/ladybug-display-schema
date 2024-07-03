"""VisualizationSet used to align geometry with data and get legends, titles, colors."""
from typing import List, Union
from enum import Enum
from pydantic import Field, constr, conint, root_validator

from .base import DisplayModes, NoExtraBaseModel, Default, Color
from .geometry2d import Vector2D, Point2D, Ray2D, LineSegment2D, \
    Polyline2D, Arc2D, Polygon2D, Mesh2D
from .geometry3d import Vector3D, Point3D, Ray3D, Plane, LineSegment3D, \
    Polyline3D, Arc3D, Face3D, Mesh3D, Polyface3D, Sphere, Cone, Cylinder
from .display2d import DisplayVector2D, DisplayPoint2D, \
    DisplayRay2D, DisplayLineSegment2D, DisplayPolyline2D, DisplayArc2D, \
    DisplayPolygon2D, DisplayMesh2D
from .display3d import DisplayVector3D, DisplayPoint3D, \
    DisplayRay3D, DisplayPlane, DisplayLineSegment3D, DisplayPolyline3D, DisplayArc3D, \
    DisplayFace3D, DisplayMesh3D, DisplayPolyface3D, DisplaySphere, DisplayCone, \
    DisplayCylinder, DisplayText3D

GEOMETRY_UNION = Union[
    Vector2D, Point2D, Ray2D, LineSegment2D, Polyline2D, Arc2D, Polygon2D,
    Mesh2D, Vector3D, Point3D, Ray3D, Plane, LineSegment3D,
    Polyline3D, Arc3D, Face3D, Mesh3D, Polyface3D, Sphere, Cone, Cylinder
]
DISPLAY_UNION = Union[
    DisplayVector2D, DisplayPoint2D, DisplayRay2D, DisplayLineSegment2D,
    DisplayPolyline2D, DisplayArc2D, DisplayPolygon2D, DisplayMesh2D,
    DisplayVector3D, DisplayPoint3D, DisplayRay3D, DisplayPlane, DisplayLineSegment3D,
    DisplayPolyline3D, DisplayArc3D, DisplayFace3D, DisplayMesh3D,
    DisplayPolyface3D, DisplaySphere, DisplayCone, DisplayCylinder, DisplayText3D
]


class Legend3DParameters(NoExtraBaseModel):

    type: constr(regex='^Legend3DParameters$') = 'Legend3DParameters'

    base_plane: Plane = Field(
        None,
        description='A Ladybug Plane object to note the starting position from '
        'where the legend will be generated. The default is the world XY plane '
        'at origin (0, 0, 0) unless the legend is assigned to a specific geometry, '
        'in which case the origin is in the lower right corner of the geometry '
        'bounding box for vertical legends and the upper right corner for '
        'horizontal legends.'
    )

    segment_height: Union[Default, float] = Field(
        Default(),
        description='A number to set the height for each of the legend segments. '
        'The default is 1 unless the legend is assigned to a specific geometry, '
        'in which case it is automatically set to a value on an appropriate scale '
        '(some fraction of the bounding box around the geometry).'
    )

    segment_width: Union[Default, float] = Field(
        Default(),
        description='A number to set the width for each of the legend segments. '
        'The default is 1 unless the legend is assigned to a specific geometry, '
        'in which case it is automatically set to a value on an appropriate scale '
        '(some fraction of the bounding box around the geometry).'
    )

    text_height: Union[Default, float] = Field(
        Default(),
        description='A number to set the height for the legend text. Default is '
        '1/3 of the segment_height.'
    )


class Legend2DParameters(NoExtraBaseModel):

    type: constr(regex='^Legend2DParameters$') = 'Legend2DParameters'

    origin_x: Union[Default, constr(regex=r'^\d*px|\d*%$')] = Field(
        Default(),
        description='A text string to note the X coordinate of the base point from '
        'where the legend will be generated (assuming an origin in the upper-left '
        'corner of the viewport with higher positive values of X moving to the right). '
        'Text must be formatted as an integer followed by either "px" (to denote '
        'the number of viewport pixels) or "%" (to denote the percentage of the '
        'viewport width). Examples include 10px, 5%. The default is set to make the '
        'legend clearly visible on the viewport (usually 10px).'
    )

    origin_y: Union[Default, constr(regex=r'^\d*px|\d*%$')] = Field(
        Default(),
        description='A text string to note the Y coordinate of the base point from '
        'where the legend will be generated (assuming an origin in the upper-left '
        'corner of the viewport with higher positive values of Y moving downward). '
        'Text must be formatted as an integer followed by either "px" (to denote '
        'the number of viewport pixels) or "%" (to denote the percentage of the '
        'viewport height). Examples include 10px, 5%. The default is set to make '
        'the legend clearly visible on the viewport (usually 50px).'
    )

    segment_height: Union[Default, constr(regex=r'^\d*px|\d*%$')] = Field(
        Default(),
        description='A text string to note the height for each of the legend '
        'segments. Text must be formatted as an integer followed by either "px" (to '
        'denote the number of viewport pixels) or "%" (to denote the percentage of the '
        'viewport height). Examples include 10px, 5%. The default is set to make most '
        'legends readable (25px for horizontal legends and 36px for vertical legends).'
    )

    segment_width: Union[Default, constr(regex=r'^\d*px|\d*%$')] = Field(
        Default(),
        description='A text string to set the width for each of the legend segments. '
        'Text must be formatted as an integer followed by either "px" (to denote '
        'the number of viewport pixels) or "%" (to denote the percentage of the '
        'viewport width). Examples include 10px, 5%. The default is set to make most '
        'legends readable (36px for horizontal legends and 25px for vertical legends).'
    )

    text_height: Union[Default, constr(regex=r'^\d*px|\d*%$')] = Field(
        Default(),
        description='A text string to set the height for the legend text. '
        'Text must be formatted as an integer followed by either "px" (to denote '
        'the number of viewport pixels) or "%" (to denote the percentage of the '
        'viewport height). Examples include 10px, 5%. Default is 1/3 of the '
        'segment_height. Default is 12px.'
    )


class LegendParameters(NoExtraBaseModel):
    """Legend parameters used to customize legends."""

    type: constr(regex='^LegendParameters$') = 'LegendParameters'

    min: Union[Default, float] = Field(
        Default(),
        description='A number to set the lower boundary of the legend. If Default, the '
        'minimum of the values associated with the legend will be used.'
    )

    max: Union[Default, float] = Field(
        Default(),
        description='A number to set the upper boundary of the legend. If Default, the '
        'maximum of the values associated with the legend will be used.'
    )

    segment_count: Union[Default, conint(ge=1)] = Field(
        Default(),
        description='An integer representing the number of steps between '
        'the high and low boundary of the legend. The default is set to 11 '
        'or it will be equal to the number of items in the ordinal_dictionary. '
        'Any custom values input in here should always be greater than or '
        'equal to 1.'
    )

    colors: List[Color] = Field(
        None,
        min_items=2,
        description='An list of color objects. Default is the Ladybug original colorset.'
    )

    title: str = Field(
        '',
        description='Text string for Legend title. Typically, the units of the data '
        'are used here but the type of data might also be used.'
    )

    continuous_legend: bool = Field(
        False,
        description='Boolean noting whether legend is drawn as a gradient or '
        'discrete segments.'
    )

    ordinal_dictionary: dict = Field(
        default=None,
        description='Optional dictionary that maps values to text categories. '
        'If None, numerical values will be used for the legend segments. If not, text '
        'categories will be used and the legend will be ordinal. Note that, if the '
        'number of items in the dictionary are less than the segment_count, some '
        'segments will not receive any label. Examples for possible dictionaries '
        'include: {-1: "Cold", 0: "Neutral", 1: "Hot"}, {0: "False", 1: "True"}'
    )

    decimal_count: conint(ge=0) = Field(
        2,
        description='An an integer for the number of decimal places in the legend '
        'text. Note that this input has no bearing on the resulting legend '
        'text when an ordinal_dictionary is present.'
    )

    include_larger_smaller: bool = Field(
        False,
        description='Boolean noting whether > and < should be included in legend '
        'segment text.'
    )

    vertical: bool = Field(
        True,
        description='Boolean noting whether legend is vertical (True) or '
        'horizontal (False).'
    )

    font: str = Field(
        'Arial',
        description='Text string to set the font for the legend text. Examples '
        'include "Arial", "Times New Roman", "Courier". Note that this '
        'parameter may not have an effect on certain interfaces that have limited '
        'access to fonts.'
    )

    properties_3d: Legend3DParameters = Field(
        None,
        description='A Legend3DParameters object to specify the dimensional '
        'properties of the legend when it is rendered in the 3D environment of '
        'the geometry scene.'
    )

    properties_2d: Legend2DParameters = Field(
        None,
        description='A Legend2DParameters object to specify the dimensional '
        'properties of the legend when it is rendered in the 2D plane of a screen.'
    )

    user_data: dict = Field(
        default=None,
        description='Optional dictionary of user data associated with the object.'
        'All keys and values of this dictionary should be of a standard data '
        'type to ensure correct serialization of the object (eg. str, float, '
        'int, list).'
    )


class DataTypes(str, Enum):
    activity_level = 'ActivityLevel'
    aerosol_optical_depth = 'AerosolOpticalDepth'
    air_speed = 'AirSpeed'
    air_temperature = 'AirTemperature'
    air_temperature_delta = 'AirTemperatureDelta'
    albedo = 'Albedo'
    angle = 'Angle'
    area = 'Area'
    atmospheric_station_pressure = 'AtmosphericStationPressure'
    ceiling_height = 'CeilingHeight'
    clothing_insulation = 'ClothingInsulation'
    convection_coefficient = 'ConvectionCoefficient'
    cooling_degree_time = 'CoolingDegreeTime'
    current = 'Current'
    dew_point_temperature = 'DewPointTemperature'
    diffuse_horizontal_illuminance = 'DiffuseHorizontalIlluminance'
    diffuse_horizontal_irradiance = 'DiffuseHorizontalIrradiance'
    diffuse_horizontal_radiation = 'DiffuseHorizontalRadiation'
    direct_horizontal_irradiance = 'DirectHorizontalIrradiance'
    direct_horizontal_radiation = 'DirectHorizontalRadiation'
    direct_normal_illuminance = 'DirectNormalIlluminance'
    direct_normal_irradiance = 'DirectNormalIrradiance'
    direct_normal_radiation = 'DirectNormalRadiation'
    discomfort_reason = 'DiscomfortReason'
    distance = 'Distance'
    dry_bulb_temperature = 'DryBulbTemperature'
    effective_radiant_field = 'EffectiveRadiantField'
    energy = 'Energy'
    energy_flux = 'EnergyFlux'
    energy_intensity = 'EnergyIntensity'
    enthalpy = 'Enthalpy'
    extraterrestrial_direct_normal_radiation = 'ExtraterrestrialDirectNormalRadiation'
    extraterrestrial_horizontal_radiation = 'ExtraterrestrialHorizontalRadiation'
    fraction = 'Fraction'
    global_horizontal_illuminance = 'GlobalHorizontalIlluminance'
    global_horizontal_irradiance = 'GlobalHorizontalIrradiance'
    global_horizontal_radiation = 'GlobalHorizontalRadiation'
    ground_temperature = 'GroundTemperature'
    heating_degree_time = 'HeatingDegreeTime'
    horizontal_infrared_radiation_intensity = 'HorizontalInfraredRadiationIntensity'
    humidity_ratio = 'HumidityRatio'
    illuminance = 'Illuminance'
    irradiance = 'Irradiance'
    liquid_precipitation_depth = 'LiquidPrecipitationDepth'
    liquid_precipitation_quantity = 'LiquidPrecipitationQuantity'
    luminance = 'Luminance'
    mass = 'Mass'
    mass_flow_rate = 'MassFlowRate'
    mean_radiant_temperature = 'MeanRadiantTemperature'
    metabolic_rate = 'MetabolicRate'
    opaque_sky_cover = 'OpaqueSkyCover'
    operative_temperature = 'OperativeTemperature'
    operative_temperature_delta = 'OperativeTemperatureDelta'
    percentage_people_dissatisfied = 'PercentagePeopleDissatisfied'
    power = 'Power'
    precipitable_water = 'PrecipitableWater'
    predicted_mean_vote = 'PredictedMeanVote'
    pressure = 'Pressure'
    prevailing_outdoor_temperature = 'PrevailingOutdoorTemperature'
    r_value = 'RValue'
    radiant_coefficient = 'RadiantCoefficient'
    radiant_temperature = 'RadiantTemperature'
    radiant_temperature_delta = 'RadiantTemperatureDelta'
    radiation = 'Radiation'
    relative_humidity = 'RelativeHumidity'
    sky_temperature = 'SkyTemperature'
    snow_depth = 'SnowDepth'
    specific_energy = 'SpecificEnergy'
    speed = 'Speed'
    standard_effective_temperature = 'StandardEffectiveTemperature'
    temperature = 'Temperature'
    temperature_delta = 'TemperatureDelta'
    temperature_time = 'TemperatureTime'
    thermal_comfort = 'ThermalComfort'
    thermal_condition = 'ThermalCondition'
    thermal_condition_eleven_point = 'ThermalConditionElevenPoint'
    thermal_condition_five_point = 'ThermalConditionFivePoint'
    thermal_condition_nine_point = 'ThermalConditionNinePoint'
    thermal_condition_seven_point = 'ThermalConditionSevenPoint'
    time = 'Time'
    total_sky_cover = 'TotalSkyCover'
    utci_category = 'UTCICategory'
    u_value = 'UValue'
    universal_thermal_climate_index = 'UniversalThermalClimateIndex'
    visibility = 'Visibility'
    voltage = 'Voltage'
    volume = 'Volume'
    volume_flow_rate = 'VolumeFlowRate'
    volume_flow_rate_intensity = 'VolumeFlowRateIntensity'
    wet_bulb_temperature = 'WetBulbTemperature'
    wind_direction = 'WindDirection'
    wind_speed = 'WindSpeed'
    zenith_luminance = 'ZenithLuminance'


class DataType(NoExtraBaseModel):
    """Data type representation."""

    type: constr(regex='^DataType$') = 'DataType'

    data_type: DataTypes = Field(
        ...,
        description='Text to indicate the type of data. This governs the behavior '
        'of the data type and the acceptable units. The DataTypes enumeration '
        'contains all acceptable types.'
    )

    name: str = Field(
        ...,
        description='Text to indicate how the data type displays. This can be more '
        'specific than the data_type.'
    )


class GenericDataType(DataType):
    """Generic data type representation."""

    type: constr(regex='^GenericDataType$') = 'GenericDataType'

    data_type: constr(regex='^GenericType$') = 'GenericType'

    base_unit: str = Field(
        ...,
        description='Text string for the base unit of the data type, which '
        'should be standard SI units where possible.'
    )

    min: Union[Default, float] = Field(
        Default(),
        description='Optional lower limit for the data type, values below which '
        'should be physically or mathematically impossible. (Default: -inf)'
    )

    max: Union[Default, float] = Field(
        Default(),
        description='Optional upper limit for the data type, values above which '
        'should be physically or mathematically impossible. (Default: +inf)'
    )

    abbreviation: str = Field(
        '',
        description='An optional abbreviation for the data type as text.'
    )

    unit_descr: dict = Field(
        default=None,
        description='An optional dictionary describing categories that the numerical '
        'values of the units relate to. For example: {-1: "Cold", 0: "Neutral", '
        '+1: "Hot"}; {0: "False", 1: "True"}.'
    )

    point_in_time: bool = Field(
        True,
        description='Boolean to note whether the data type represents conditions '
        'at a single instant in time (True) as opposed to being an average or '
        'accumulation over time (False) when it is found in hourly lists of data.'
    )

    cumulative: bool = Field(
        False,
        description='Boolean to tell whether the data type can be cumulative when '
        'it is represented over time (True) or it can only be averaged over time '
        'to be meaningful (False). Note that cumulative cannot be True when '
        'point_in_time is also True.'
    )


class VisualizationData(NoExtraBaseModel):
    """Represents a data set for visualization with legend parameters and data type."""

    type: constr(regex='^VisualizationData$') = 'VisualizationData'

    values: List[float] = Field(
        ...,
        min_items=1,
        description='A list of numerical values that will be used to generate '
        'the visualization colors.'
    )

    legend_parameters: LegendParameters = Field(
        None,
        description='An Optional LegendParameters object to override default '
        'parameters of the legend. None indicates that default legend parameters '
        'will be used.'
    )

    data_type: Union[DataType, GenericDataType] = Field(
        None,
        description='Optional DataType from the ladybug datatype subpackage (ie. '
        'Temperature()) , which will be used to assign default legend properties. '
        'If None, the legend associated with this object will contain no units '
        'unless a unit below is specified.'
    )

    unit: str = Field(
        '',
        description='Optional text string for the units of the values. (ie. "C"). '
        'If None, the default units of the data_type will be used.'
    )

    user_data: dict = Field(
        default=None,
        description='Optional dictionary of user data associated with the object.'
        'All keys and values of this dictionary should be of a standard data '
        'type to ensure correct serialization of the object (eg. str, float, '
        'int, list).'
    )


class VisualizationMetaData(NoExtraBaseModel):
    """Represents the visualization metadata that can be assigned to VisualizationData.
    """

    type: constr(regex='^VisualizationMetaData$') = 'VisualizationMetaData'

    legend_parameters: LegendParameters = Field(
        None,
        description='An Optional LegendParameters object to override default '
        'parameters of the legend. None indicates that default legend parameters '
        'will be used.'
    )

    data_type: Union[DataType, GenericDataType] = Field(
        None,
        description='Optional DataType from the ladybug datatype subpackage (ie. '
        'Temperature()) , which will be used to assign default legend properties. '
        'If None, the legend associated with this object will contain no units '
        'unless a unit below is specified.'
    )

    unit: str = Field(
        '',
        description='Optional text string for the units of the values. (ie. "C"). '
        'If None, the default units of the data_type will be used.'
    )

    user_data: dict = Field(
        default=None,
        description='Optional dictionary of user data associated with the object.'
        'All keys and values of this dictionary should be of a standard data '
        'type to ensure correct serialization of the object (eg. str, float, '
        'int, list).'
    )


class _VisualizationBase(NoExtraBaseModel):
    """Base class for visualization objects."""

    identifier: str = Field(
        ...,
        regex=r'^[.A-Za-z0-9_-]+$',
        min_length=1,
        max_length=100,
        description='Text string for a unique object ID. Must be less than 100 '
        'characters and not contain spaces or special characters.'
    )

    display_name: str = Field(
        default=None,
        description='Display name of the object with no character restrictions. '
        'This is typically used to set the layer of the object in the interface that '
        'renders the VisualizationSet. A :: in the display_name can be used to denote '
        'sub-layers following a convention of ParentLayer::SubLayer. If not set, '
        'the display_name will be equal to the object identifier.'
    )

    user_data: dict = Field(
        default=None,
        description='Optional dictionary of user data associated with the object.'
        'All keys and values of this dictionary should be of a standard data '
        'type to ensure correct serialization of the object (eg. str, float, '
        'int, list).'
    )


class AnalysisGeometry(_VisualizationBase):
    """An object where multiple data streams correspond to the same geometry."""

    type: constr(regex='^AnalysisGeometry$') = 'AnalysisGeometry'

    geometry: List[GEOMETRY_UNION] = Field(
        ...,
        description='A list of ladybug-geometry objects that is aligned with the '
        'values in the input data_sets. The length of this list should usually be equal '
        'to the total number of values in each data_set, indicating that each geometry '
        'gets a single color. Alternatively, if all of the geometry objects are '
        'meshes, the number of values in the data can be equal to the total number of '
        'faces across the meshes or the total number of vertices across the meshes.'
    )

    data_sets: List[VisualizationData] = Field(
        ...,
        min_items=1,
        description='An list of VisualizationData objects representing the data sets '
        'that are associated with the input geometry.'
    )

    active_data: int = Field(
        0,
        description='An integer to denote which of the input data_sets should be '
        'displayed by default.'
    )

    display_mode: DisplayModes = Field(
        DisplayModes.surface,
        description='Text to indicate the display mode (surface, wireframe, '
        'etc.). The DisplayModes enumeration contains all acceptable types.'
    )

    hidden: bool = Field(
        False,
        description='A boolean to note whether the geometry is hidden by default '
        'and must be un-hidden to be visible in the 3D scene.'
    )

    @root_validator
    def check_values_align(cls, obj_props):
        """Check that values and geometry align."""
        data_sets, geos = obj_props.get('data_sets'), obj_props.get('geometry')
        geo_count_0, geo_count_1, geo_count_2 = len(geos), 0, 0
        for geo in geos:
            if isinstance(geo, (Mesh2D, Mesh3D)):
                geo_count_1 += len(geo.faces)
                geo_count_2 += len(geo.vertices)
        possible_lens = (geo_count_0, geo_count_1, geo_count_2)
        assert len(data_sets[0].values) in possible_lens, 'Expected number of values' \
            ' ({}) to align with the number of geometries ({}), the number of ' \
            'mesh faces ({}), or the number of mesh vertices ({}).'.format(
                len(data_sets[0].values), geo_count_0, geo_count_1, geo_count_2)
        ref_len = len(data_sets[0].values)
        for data in data_sets[1:]:
            assert len(data.values) == ref_len, 'Expected all data sets of ' \
                'AnalysisGeometry to have the same length. {} != {}.'.format(
                    len(data.values), ref_len)
        return obj_props


class ContextGeometry(_VisualizationBase):
    """An object representing context geometry to display."""

    type: constr(regex='^ContextGeometry$') = 'ContextGeometry'

    geometry: List[DISPLAY_UNION] = Field(
        ...,
        description='A list of ladybug-geometry or ladybug-display objects that gives '
        'context to analysis geometry or other aspects of the visualization. '
        'Typically, these will display in wireframe around the geometry, though '
        'the properties of display geometry can be used to customize the '
        'visualization.'
    )

    hidden: bool = Field(
        False,
        description='A boolean to note whether the geometry is hidden by default '
        'and must be un-hidden to be visible in the 3D scene.'
    )


class Units(str, Enum):
    meters = 'Meters'
    millimeters = 'Millimeters'
    feet = 'Feet'
    inches = 'Inches'
    centimeters = 'Centimeters'


class VisualizationSet(_VisualizationBase):
    """A visualization set containing analysis and context geometry to be visualized."""

    type: constr(regex='^VisualizationSet$') = 'VisualizationSet'

    geometry: List[Union[AnalysisGeometry, ContextGeometry]] = Field(
        None,
        description='A list of AnalysisGeometry and ContextGeometry objects to '
        'display in the visualization. Each geometry object will typically be '
        'translated to its own layer within the interface that renders the '
        'VisualizationSet.'
    )

    units: Units = Field(
        default=None,
        description='Text indicating the units in which the model geometry exists. '
        'If None, the geometry will always be assumed to be in the current units '
        'system of the display interface.'
    )
