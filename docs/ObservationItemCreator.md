# ObservationItemCreator

User that created the Observation Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**name** | **str** | User Name | [optional] 
**login** | **str** | Email | [optional] 
**vendor** | [**ObservationItemCreatorSCompany**](ObservationItemCreatorSCompany.md) |  | [optional] 

## Example

```python
from procore_sdk.models.observation_item_creator import ObservationItemCreator

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemCreator from a JSON string
observation_item_creator_instance = ObservationItemCreator.from_json(json)
# print the JSON string representation of the object
print(ObservationItemCreator.to_json())

# convert the object into a dict
observation_item_creator_dict = observation_item_creator_instance.to_dict()
# create an instance of ObservationItemCreator from a dict
observation_item_creator_from_dict = ObservationItemCreator.from_dict(observation_item_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


