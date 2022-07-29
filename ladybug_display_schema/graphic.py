"""Graphic container used to get legends, titles, and colors for any graphic."""
from typing import List, Union
from enum import Enum
from pydantic import Field, constr, conint, root_validator

from .base import NoExtraBaseModel, Default, Color
from .geometry2d import Vector2D, Point2D, Ray2D, LineSegment2D, \
    Polyline2D, Arc2D, Polygon2D, Mesh2D
from .geometry3d import Vector3D, Point3D, Ray3D, Plane, LineSegment3D, \
    Polyline3D, Arc3D, Face3D, Mesh3D, Polyface3D, Sphere, Cone, Cylinder


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


class GraphicContainer(NoExtraBaseModel):
    """Graphic container used to get legends, titles, and colors for any graphic."""

    type: constr(regex='^GraphicContainer$') = 'GraphicContainer'

    values: List[float] = Field(
        ...,
        min_items=1,
        description='An list of numerical values that will be used to generate '
        'the legend and colors.'
    )

    geometry: Union[Mesh2D, Mesh3D, Polyface3D, List[Union[
        Vector2D, Point2D, Ray2D, LineSegment2D, Polyline2D, Arc2D, Polygon2D,
        Mesh2D, Vector3D, Point3D, Ray3D, Plane, LineSegment3D,
        Polyline3D, Arc3D, Face3D, Mesh3D, Polyface3D, Sphere, Cone, Cylinder
    ]]] = Field(
        None,
        description='An optional ladybug-geometry object (or list of ladybug-geometry '
        'objects) that is aligned with the input values. If a Mesh or Polyface '
        'is specified here, it is expected that the number of values match the '
        'number of faces or the number of vertices. If a list of geometry objects '
        'is specified (ie. a list of Point3Ds), it is expected that the length '
        'of this list align with the number of values.'
    )

    min_point: Point3D = Field(
        None,
        description='A Point3D object for the minimum of the bounding box around '
        'the graphic geometry. If None, then there must be an input for geometry '
        'and the bounding box around this geometry will be used to set up the '
        'graphic container.'
    )

    max_point: Point3D = Field(
        None,
        description='A Point3D object for the maximum of the  bounding box around '
        'the graphic geometry. If None, then there must be an input for geometry '
        'and the bounding box around this geometry will be used to set up the '
        'graphic container.'
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

    @root_validator
    def check_values_align(cls, obj_props):
        """Check that values and geometry align."""
        values, geo = obj_props.get('values'), obj_props.get('geometry')
        if isinstance(geo, (Mesh2D, Mesh3D, Polyface3D)):
            if isinstance(geo, (Mesh2D, Mesh3D)):
                assert len(values) == len(geo.faces) or len(values) == \
                    len(geo.vertices), 'Expected number of values ({}) to match ' \
                    'number of faces ({}) or number of vertices ({}).'.format(
                        len(values), len(geo.faces), len(geo.vertices))
            else:  # it's a Polyface3D
                assert len(values) == len(geo.face_indices) or len(values) == \
                    len(geo.vertices), 'Expected number of values ({}) to match ' \
                    'number of faces ({}) or number of vertices ({}).'.format(
                        len(values), len(geo.face_indices), len(geo.vertices))
        else:  # make sure that there are min and max points
            min_point, max_point = obj_props.get('min_point'), obj_props.get('max_point')
            assert min_point is not None and max_point is not None, \
                'If min_point or max_point are unspecified, then geometry must be a ' \
                'Mesh or Polyface to determine the bounding box.'
            if isinstance(geo, (list, tuple)):
                assert len(values) == len(geo), 'Expected one value per geometry ' \
                    'when geometry is a list. Number of values ({}) does not match ' \
                    'number of geometries ({}).'.format(len(values), len(geo))
        return obj_props
