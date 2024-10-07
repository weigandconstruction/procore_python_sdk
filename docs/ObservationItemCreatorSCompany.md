# ObservationItemCreatorSCompany

Company of User that created the Observation Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Vendor ID | [optional] 
**name** | **str** | Vendor Name | [optional] 

## Example

```python
from procore_sdk.models.observation_item_creator_s_company import ObservationItemCreatorSCompany

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemCreatorSCompany from a JSON string
observation_item_creator_s_company_instance = ObservationItemCreatorSCompany.from_json(json)
# print the JSON string representation of the object
print(ObservationItemCreatorSCompany.to_json())

# convert the object into a dict
observation_item_creator_s_company_dict = observation_item_creator_s_company_instance.to_dict()
# create an instance of ObservationItemCreatorSCompany from a dict
observation_item_creator_s_company_from_dict = ObservationItemCreatorSCompany.from_dict(observation_item_creator_s_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


