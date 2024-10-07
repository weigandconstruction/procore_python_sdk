# WorkClassificationBulkBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_classification** | [**WorkClassification1**](WorkClassification1.md) |  | 

## Example

```python
from procore_sdk.models.work_classification_bulk_body import WorkClassificationBulkBody

# TODO update the JSON string below
json = "{}"
# create an instance of WorkClassificationBulkBody from a JSON string
work_classification_bulk_body_instance = WorkClassificationBulkBody.from_json(json)
# print the JSON string representation of the object
print(WorkClassificationBulkBody.to_json())

# convert the object into a dict
work_classification_bulk_body_dict = work_classification_bulk_body_instance.to_dict()
# create an instance of WorkClassificationBulkBody from a dict
work_classification_bulk_body_from_dict = WorkClassificationBulkBody.from_dict(work_classification_bulk_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


