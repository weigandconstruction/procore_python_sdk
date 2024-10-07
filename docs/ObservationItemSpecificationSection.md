# ObservationItemSpecificationSection

Specification Section

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**description** | **str** | Description | [optional] 
**number** | **str** | Number | [optional] 
**latest_revision_url** | **str** | Url to PDF view | [optional] 

## Example

```python
from procore_sdk.models.observation_item_specification_section import ObservationItemSpecificationSection

# TODO update the JSON string below
json = "{}"
# create an instance of ObservationItemSpecificationSection from a JSON string
observation_item_specification_section_instance = ObservationItemSpecificationSection.from_json(json)
# print the JSON string representation of the object
print(ObservationItemSpecificationSection.to_json())

# convert the object into a dict
observation_item_specification_section_dict = observation_item_specification_section_instance.to_dict()
# create an instance of ObservationItemSpecificationSection from a dict
observation_item_specification_section_from_dict = ObservationItemSpecificationSection.from_dict(observation_item_specification_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


