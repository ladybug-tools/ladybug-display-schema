"""VisualizationSet used to align geometry with data and get legends, titles, colors."""
from typing import List, Union
from enum import Enum
from pydantic import Field, constr, conint, root_validator

from .base import NoExtraBaseModel, Default, Color
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
    DisplayCylinder

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
    DisplayPolyface3D, DisplaySphere, DisplayCone, DisplayCylinder
]


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

    segment_count: Union[Default, conint(ge=2)] = Field(
        Default(),
        description='An integer representing the number of steps between '
        'the high and low boundary of the legend. The default is set to 11 '
        'or it will be equal to the number of items in the ordinal_dictionary. '
        'Any custom values input in here should always be greater than or '
        'equal to 2.'
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

    base_plane: Plane = Field(
        None,
        description='A Ladybug Plane object to note the starting point from '
        'where the legend will be generated. The default is the world XY plane '
        'at origin (0, 0, 0).'
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

    segment_height: Union[Default, float] = Field(
        Default(),
        description='A number to set the height for each of the legend segments.'
    )

    segment_width: Union[Default, float] = Field(
        Default(),
        description='A number to set the width for each of the legend segments.'
    )

    text_height: Union[Default, float] = Field(
        Default(),
        description='A number to set the height for the legend text. Default is '
        '1/3 of the segment_height.'
    )

    font: str = Field(
        'Arial',
        description='Text string to set the font for the legend text. Examples '
        'include "Arial", "Times New Roman", "Courier". Note that this '
        'parameter may not have an effect on certain interfaces that have limited '
        'access to fonts.'
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

    data_type: DataType = Field(
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


class AnalysisGeometry(NoExtraBaseModel):
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

    user_data: dict = Field(
        default=None,
        description='Optional dictionary of user data associated with the object.'
        'All keys and values of this dictionary should be of a standard data '
        'type to ensure correct serialization of the object (eg. str, float, '
        'int, list).'
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


class VisualizationSet(NoExtraBaseModel):
    """A visualization set containing analysis and context geometry to be visualized."""

    type: constr(regex='^VisualizationSet$') = 'VisualizationSet'

    analysis_geometry: List[AnalysisGeometry] = Field(
        None,
        description='A list of AnalysisGeometry objects for spatial data that is '
        'displayed in the visualization. Multiple AnalysisGeometry objects can '
        'be used to specify different related studies that were run to create '
        'the visualization (eg. a radiation study of windows next to a daylight '
        'study of interior floor plates).'
    )

    context_geometry: List[DISPLAY_UNION] = Field(
        None,
        description='An optional list of ladybug-geometry or ladybug-display objects '
        'that gives context to the analysis geometry or other aspects of the '
        'visualization. Typically, these will display in wireframe around the '
        'geometry, though the properties of display geometry can be used to '
        'customize the visualization.'
    )

    user_data: dict = Field(
        default=None,
        description='Optional dictionary of user data associated with the object.'
        'All keys and values of this dictionary should be of a standard data '
        'type to ensure correct serialization of the object (eg. str, float, '
        'int, list).'
    )
