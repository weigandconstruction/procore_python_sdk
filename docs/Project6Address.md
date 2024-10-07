# Project6Address

Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | street name | [optional] 
**city** | **str** | City | [optional] 
**state_code** | **str** | State code | [optional] 
**zip** | **str** | Zip code | [optional] 
**country_code** | **str** | CityCountry code | [optional] 

## Example

```python
from procore_sdk.models.project6_address import Project6Address

# TODO update the JSON string below
json = "{}"
# create an instance of Project6Address from a JSON string
project6_address_instance = Project6Address.from_json(json)
# print the JSON string representation of the object
print(Project6Address.to_json())

# convert the object into a dict
project6_address_dict = project6_address_instance.to_dict()
# create an instance of Project6Address from a dict
project6_address_from_dict = Project6Address.from_dict(project6_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


