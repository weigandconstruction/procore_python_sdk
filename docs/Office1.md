# Office1

Office

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Office id | [optional] 
**name** | **str** | Office name | [optional] 
**address** | **str** | Office address | [optional] 
**city** | **str** | Office city | [optional] 
**state_code** | **str** | Office state code (ISO-3166 Alpha-2 format) | [optional] 
**country_code** | **str** | Office country code (ISO-3166 Alpha-2 format) | [optional] 
**zip** | **str** | Office zip | [optional] 
**phone** | **str** | Office phone | [optional] 
**fax** | **str** | Office fax | [optional] 
**division** | **str** | Office division | [optional] 
**logo** | [**RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.office1 import Office1

# TODO update the JSON string below
json = "{}"
# create an instance of Office1 from a JSON string
office1_instance = Office1.from_json(json)
# print the JSON string representation of the object
print(Office1.to_json())

# convert the object into a dict
office1_dict = office1_instance.to_dict()
# create an instance of Office1 from a dict
office1_from_dict = Office1.from_dict(office1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


