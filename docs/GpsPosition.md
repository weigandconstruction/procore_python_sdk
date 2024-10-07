# GpsPosition

Gps Position object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitude in degrees. | 
**longitude** | **float** | The longitude in degrees. | 
**altitude** | **float** | The altitude, measured in meters. | [optional] 
**horizontal_accuracy** | **float** | The horizontal radius of uncertainty for the location, measured in meters. | [optional] 
**vertical_accuracy** | **float** | The vertical radius of uncertainty for the location, measured in meters. | [optional] 
**timestamp** | **datetime** | The time at which this location was determined. | 

## Example

```python
from procore_sdk.models.gps_position import GpsPosition

# TODO update the JSON string below
json = "{}"
# create an instance of GpsPosition from a JSON string
gps_position_instance = GpsPosition.from_json(json)
# print the JSON string representation of the object
print(GpsPosition.to_json())

# convert the object into a dict
gps_position_dict = gps_position_instance.to_dict()
# create an instance of GpsPosition from a dict
gps_position_from_dict = GpsPosition.from_dict(gps_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


