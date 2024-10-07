# InspectorCompany

Company

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Company ID | [optional] 
**name** | **str** | Company name | [optional] 

## Example

```python
from procore_sdk.models.inspector_company import InspectorCompany

# TODO update the JSON string below
json = "{}"
# create an instance of InspectorCompany from a JSON string
inspector_company_instance = InspectorCompany.from_json(json)
# print the JSON string representation of the object
print(InspectorCompany.to_json())

# convert the object into a dict
inspector_company_dict = inspector_company_instance.to_dict()
# create an instance of InspectorCompany from a dict
inspector_company_from_dict = InspectorCompany.from_dict(inspector_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


