# ProjectOffice3


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
from procore_sdk.models.project_office3 import ProjectOffice3

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectOffice3 from a JSON string
project_office3_instance = ProjectOffice3.from_json(json)
# print the JSON string representation of the object
print(ProjectOffice3.to_json())

# convert the object into a dict
project_office3_dict = project_office3_instance.to_dict()
# create an instance of ProjectOffice3 from a dict
project_office3_from_dict = ProjectOffice3.from_dict(project_office3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


