# TimesheetsSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**signature_text** | **str** | Acknowedgement text the signature was signed against. | [optional] 
**file_name** | **str** | File Name | [optional] 
**url** | **str** | URL | [optional] 
**medium_thumbnail_url** | **str** | URL | [optional] 
**large_thumbnail_url** | **str** | URL | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.timesheets_signature import TimesheetsSignature

# TODO update the JSON string below
json = "{}"
# create an instance of TimesheetsSignature from a JSON string
timesheets_signature_instance = TimesheetsSignature.from_json(json)
# print the JSON string representation of the object
print(TimesheetsSignature.to_json())

# convert the object into a dict
timesheets_signature_dict = timesheets_signature_instance.to_dict()
# create an instance of TimesheetsSignature from a dict
timesheets_signature_from_dict = TimesheetsSignature.from_dict(timesheets_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


