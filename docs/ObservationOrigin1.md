# ObservationOrigin1

Inspection (Checklist List) that the Observation Item was created from

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Origin Type | [optional] 
**payload** | [**OriginPayload1**](OriginPayload1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation_origin1 import ObservationOrigin1

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationOrigin1 from a JSON string
observation_origin1_instance = ObservationOrigin1.from_json(json)
# print the JSON string representation of the object
print(ObservationOrigin1.to_json())

# convert the object into a dict
observation_origin1_dict = observation_origin1_instance.to_dict()
# create an instance of ObservationOrigin1 from a dict
observation_origin1_from_dict = ObservationOrigin1.from_dict(observation_origin1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


