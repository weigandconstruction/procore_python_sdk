# ExtendedView

Company signee party

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_id** | **str** | Employee ID for the Party Person | [optional] 
**first_name** | **str** | Party Person first name | [optional] 
**id** | **int** | Unique identifier for the Party Person. | [optional] 
**is_employee** | **bool** | Employee status for the Party Person | [optional] 
**last_name** | **str** | Party Person last name | [optional] 
**user_id** | **int** | User ID if this Party Person represents a User. NULL for a Reference User. | [optional] 
**work_classification** | [**ExtendedViewWorkClassification**](ExtendedViewWorkClassification.md) |  | [optional] 

## Example

```python
from procore_sdk.models.extended_view import ExtendedView

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedView from a JSON string
extended_view_instance = ExtendedView.from_json(json)
# print the JSON string representation of the object
print(ExtendedView.to_json())

# convert the object into a dict
extended_view_dict = extended_view_instance.to_dict()
# create an instance of ExtendedView from a dict
extended_view_from_dict = ExtendedView.from_dict(extended_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


