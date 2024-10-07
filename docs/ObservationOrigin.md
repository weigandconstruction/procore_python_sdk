# ObservationOrigin

Origin Item that the Observation was created from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Origin Type | [optional] 
**payload** | [**OriginPayload**](OriginPayload.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation_origin import ObservationOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationOrigin from a JSON string
observation_origin_instance = ObservationOrigin.from_json(json)
# print the JSON string representation of the object
print(ObservationOrigin.to_json())

# convert the object into a dict
observation_origin_dict = observation_origin_instance.to_dict()
# create an instance of ObservationOrigin from a dict
observation_origin_from_dict = ObservationOrigin.from_dict(observation_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


