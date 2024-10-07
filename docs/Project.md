# Project

Project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Project Id | [optional] 
**country_code** | **str** | Country Code | [optional] 
**country_name** | **str** | Country Name | [optional] 
**state_code** | **str** | State Code | [optional] 
**state_name** | **str** | State Name | [optional] 
**county** | **str** | County | [optional] 
**city** | **str** | City | [optional] 
**address** | **str** | Address | [optional] 
**zip** | **str** | ZIP | [optional] 
**phone** | **str** | Phone | [optional] 
**fax** | **str** | Fax | [optional] 
**time_zone** | **str** | Time Zone | [optional] 
**time_zone_name** | **str** | Time Zone Name | [optional] 
**logo_url** | **str** | Logo URL | [optional] 

## Example

```python
from procore_sdk.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


