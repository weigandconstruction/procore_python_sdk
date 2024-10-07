# DepartmentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | Company ID | 
**department** | [**Department**](Department.md) |  | 

## Example

```python
from procore_sdk.models.department_body import DepartmentBody

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentBody from a JSON string
department_body_instance = DepartmentBody.from_json(json)
# print the JSON string representation of the object
print(DepartmentBody.to_json())

# convert the object into a dict
department_body_dict = department_body_instance.to_dict()
# create an instance of DepartmentBody from a dict
department_body_from_dict = DepartmentBody.from_dict(department_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


