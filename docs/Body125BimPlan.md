# Body125BimPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_level_id** | **int** | ID of the BIM Level to be associated to the plan | 
**drawing_id** | **int** | ID of the Drawing to be associated to the plan | [optional] 
**upload_uuid** | **str** | UUID of uploaded 2D sheet image. One of drawing_id or upload_uid is required | [optional] 
**sheet_map_start** | [**RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart**](RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart.md) |  | [optional] 
**sheet_map_end** | [**RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart**](RestV10BimPlansGet200ResponseInnerAllOfSheetMapStart.md) |  | [optional] 
**model_map_start** | [**RestV10BimPlansGet200ResponseInnerAllOfModelMapStart**](RestV10BimPlansGet200ResponseInnerAllOfModelMapStart.md) |  | [optional] 
**model_map_end** | [**RestV10BimPlansGet200ResponseInnerAllOfModelMapStart**](RestV10BimPlansGet200ResponseInnerAllOfModelMapStart.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body125_bim_plan import Body125BimPlan

# TODO update the JSON string below
json = "{}"
# create an instance of Body125BimPlan from a JSON string
body125_bim_plan_instance = Body125BimPlan.from_json(json)
# print the JSON string representation of the object
print(Body125BimPlan.to_json())

# convert the object into a dict
body125_bim_plan_dict = body125_bim_plan_instance.to_dict()
# create an instance of Body125BimPlan from a dict
body125_bim_plan_from_dict = Body125BimPlan.from_dict(body125_bim_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


