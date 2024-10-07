# ProjectOffice1

Office associated to the project or company main office if project does not set an office

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The identifier for the Office | [optional] 
**name** | **str** | The name for the Office | [optional] 
**address** | **str** | Office address | [optional] 
**city** | **str** | Office city | [optional] 
**state_code** | **str** | Office state code (ISO-3166 Alpha-2 format) | [optional] 
**country_code** | **str** | Office country code (ISO-3166 Alpha-2 format) | [optional] 
**zip** | **str** | Office zip | [optional] 
**phone** | **str** | Office phone | [optional] 
**fax** | **str** | Office fax | [optional] 
**division** | **str** | Office division | [optional] 
**logo** | [**RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner**](RestV11ProjectsProjectIdDailyLogsWeatherLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.project_office1 import ProjectOffice1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectOffice1 from a JSON string
project_office1_instance = ProjectOffice1.from_json(json)
# print the JSON string representation of the object
print(ProjectOffice1.to_json())

# convert the object into a dict
project_office1_dict = project_office1_instance.to_dict()
# create an instance of ProjectOffice1 from a dict
project_office1_from_dict = ProjectOffice1.from_dict(project_office1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


