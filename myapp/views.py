from django.shortcuts import render,render_to_response
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from  myapp.models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import simplejson
from decimal import *
import csv, os
import xlrd, xlwt
from xlwt import Workbook


@csrf_exempt
def index(request):
    if request.POST:
        droppipe_size = request.POST.get('droppipe_size')
        droppipe_material = request.POST.get('droppipe_material')
        droppipe_Piping = request.POST.get('droppipe_Piping')
        droppipe_length = request.POST.get('droppipe_length')
        price_droppipe = request.POST.get('price_droppipe')
        desc_propipe = []
        dropipe_des1 = Material.objects.filter(id=int(droppipe_material))[0].material
        dropipe_des2 = Piping.objects.filter(id=int(droppipe_Piping))[0].piping
        dropipe_des3 = Size.objects.filter(id=int(droppipe_size))[0].size

        desc_propipe.append(dropipe_des1)
        desc_propipe.append(dropipe_des2)
        desc_propipe.append(dropipe_des3)
        desc_propipe = ",".join(desc_propipe)

        droppipe_asses_assessories = request.POST.getlist('droppipe_accessories', None)
        droppipe_access_size = request.POST.getlist('access_size', None)
        droppipe_access_type = request.POST.getlist('access_type', None)
        droppipe_droppipe_price = request.POST.getlist('droppipe_price', 0)
        droppipe_droppipe_quantity = request.POST.getlist('droppipe_quantity', 0)
        droppipe_asses_assessories_list = []
        if droppipe_asses_assessories:
            for i in droppipe_asses_assessories:
                data = Accessories.objects.filter(id=int(i))
                if data:
                    droppipe_asses_assessories_list.append(data[0].name)

        all_propipe_access = zip(droppipe_asses_assessories_list, droppipe_access_size, droppipe_access_type,
                                 droppipe_droppipe_quantity, droppipe_droppipe_price)
        total_dropipe_ass_price = 0.0
        total_dropipe_ass_quantity = 0
        for i in droppipe_droppipe_price:
            total_dropipe_ass_price = Decimal(total_dropipe_ass_price) + Decimal(i)
        for i in droppipe_droppipe_quantity:
            total_dropipe_ass_quantity = int(total_dropipe_ass_quantity) + int(i)

        manifold_size = request.POST.get('manifold_size')
        manifold_material = request.POST.get('manifold_material')
        manifold_piping = request.POST.get('manifold_Piping')
        manifold_length = request.POST.get('manifold_length')
        price_manifold = request.POST.get('price_manifold')
        desc_manifold = []

        manifold_des1 = Material.objects.filter(id=int(manifold_material))[0].material
        manifold_des2 = Piping.objects.filter(id=int(manifold_piping))[0].piping
        manifold_des3 = Size.objects.filter(id=int(manifold_size))[0].size
        print ">>>>>>>>>", manifold_des1
        desc_manifold.append(str(manifold_des1))
        desc_manifold.append(manifold_des2)
        desc_manifold.append(manifold_des3)
        desc_manifold = ",".join(desc_manifold)

        manifold_asses_assessories = request.POST.getlist('manifold_accessories', None)
        manifold_access_size = request.POST.getlist('access_manifold_size', None)
        manifold_access_type = request.POST.getlist('access_manifold_type', None)
        manifold_price = request.POST.getlist('manifold_access_price', 0)
        manifold_quantity = request.POST.getlist('manifold_access_quntity', 0)
        manifold_asses_assessories_list = []
        if manifold_asses_assessories:
            for i in manifold_asses_assessories:
                data = Accessories.objects.filter(id=int(i))
                if data:
                    manifold_asses_assessories_list.append(data[0].name)
        all_manifold_access = zip(manifold_asses_assessories_list, manifold_access_size, manifold_access_type,
                                  manifold_price, manifold_quantity)
        total_manifold_ass_price = 0.0
        total_manifold_ass_quantity = 0
        for i in manifold_price:
            total_manifold_ass_price = Decimal(total_manifold_ass_price) + Decimal(i)
        for i in manifold_quantity:
            total_manifold_ass_quantity = int(total_manifold_ass_quantity) + int(i)

        headers_size = request.POST.get('headers_size')
        headers_material = request.POST.get('headers_material')
        headers_Piping = request.POST.get('headers_Piping')
        headers_length = request.POST.get('headers_length')
        price_header = request.POST.get('price_header')
        desc_header = []
        header_des1 = Material.objects.filter(id=int(headers_material))[0].material
        header_des2 = Piping.objects.filter(id=int(headers_Piping))[0].piping
        header_des3 = Size.objects.filter(id=int(headers_size))[0].size
        desc_header.append(header_des1)
        desc_header.append(header_des2)
        desc_header.append(header_des3)
        desc_header = ",".join(desc_header)

        header_asses_assessories = request.POST.getlist('headers_accessories', None)
        header_access_size = request.POST.getlist('headers_size', None)
        header_access_type = request.POST.getlist('headers_type', None)
        header_price = request.POST.getlist('header_access_price', 0)
        header_quantity = request.POST.getlist('header_access_quntity', 0)
        header_asses_assessories_list = []
        if header_asses_assessories:
            for i in header_asses_assessories:
                data = Accessories.objects.filter(id=int(i))
                if data:
                    header_asses_assessories_list.append(data[0].name)
        all_header_access = zip(header_asses_assessories_list, header_access_size, header_access_type, header_price,
                                header_quantity)
        total_header_ass_price = 0.0
        total_header_ass_quantity = 0
        for i in header_price:
            total_header_ass_price = Decimal(total_header_ass_price) + Decimal(i)
        for i in header_quantity:
            total_header_ass_quantity = int(total_header_ass_quantity) + int(i)
        total_price = Decimal(price_droppipe) + Decimal(price_manifold) + Decimal(price_header) + Decimal(
            total_header_ass_price) + Decimal(total_manifold_ass_price) + Decimal(total_dropipe_ass_price)
        # description = []
        # description.append(des1)
        # description.append(des2)
        # description.append(des3)
        # final_description = ",".join(description)
        # total_price_obj = TotalCost()
        # total_price_obj.description = final_description
        # total_price_obj.unit_price = 0
        # total_price_obj.quantity = total_quantity
        # total_price_obj.total_price = total_price
        # total_price_obj.save()
        # return total_price_obj
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="estimation_report.csv"'
        writer = csv.writer(response)
        writer.writerow(["Description", "Total Quantity", "Total Price"])
        item = 1
        writer.writerow([str(desc_propipe), int(droppipe_length), Decimal(price_droppipe)])

        for i in all_propipe_access:
            item = item+1
            desc_o =[]
            desc_o.append(i[0])
            desc_o.append(i[1])
            desc_o.append(i[2])
            desc_o =  ",".join(desc_o)
            writer.writerow([str(desc_o), str(i[3]), str(i[4])])
        item =item+1
        writer.writerow([str(desc_manifold), int(manifold_length), Decimal(price_manifold)])
        for i in all_manifold_access:
            item = item + 1
            desc_o = []
            desc_o.append(i[0])
            desc_o.append(i[1])
            desc_o.append(i[2])
            desc_o = ",".join(desc_o)
            writer.writerow([str(desc_o), str(i[4]), str(i[3])])
        item = item + 1
        writer.writerow([ str(desc_header), int(headers_length), Decimal(price_header)])
        for i in all_header_access:
            item = item + 1
            desc_o = []
            desc_o.append(i[0])
            desc_o.append(i[1])
            desc_o.append(i[2])
            desc_o = ",".join(desc_o)
            writer.writerow([str(desc_o), str(i[4]), str(i[3])])
        writer.writerow(['',str('Total Price'),str(total_price)])
        return response
        # excel_id = None
        # total_price = None
        # size = Size.objects.filter(active=True)
        # material = Material.objects.filter(active=True)
        # piping = Piping.objects.filter(active=True)
        # accessories_droppipe = Accessories.objects.filter(active=True,id__in=[1,2,12,13])
        # accessories_manifold = Accessories.objects.filter(active=True)
        # accessories_headers = Accessories.objects.filter(active=True,id__in=[1,2,8])
        # accessories = Accessories.objects.filter(active=True)
        # return render(request, 'index.html',{'size':size,'material':material,'piping':piping,'accessories':accessories,'accessories_droppipe':accessories_droppipe,
        #                                      'accessories_manifold':accessories_manifold,'accessories_headers':accessories_headers,'total_price':total_price,'excel_id':excel_id},
        #               context_instance=RequestContext(request))
    else:
        size = Size.objects.filter(active=True)
        material = Material.objects.filter(active=True)
        piping = Piping.objects.filter(active=True)
        accessories_droppipe = Accessories.objects.filter(active=True, id__in=[1, 2, 12, 13])
        accessories_manifold = Accessories.objects.filter(active=True)
        accessories_headers = Accessories.objects.filter(active=True, id__in=[1, 2, 8])
        accessories = Accessories.objects.filter(active=True)
        return render(request, 'index.html',
                      {'size': size, 'material': material, 'piping': piping, 'accessories': accessories,
                       'accessories_droppipe': accessories_droppipe,
                       'accessories_manifold': accessories_manifold, 'accessories_headers': accessories_headers},
                      context_instance=RequestContext(request))
@csrf_exempt
def droppipe_accessories(request):
    output ={}
    access_id = request.POST.get('selected_acc')
    access_size = AccessoriesSize.objects.filter(accessories_id=int(access_id))
    access_type = AccessoriesType.objects.filter(accessories_id=int(access_id)).values_list('type', flat=True)
    sizelist =  []
    if access_size:
        for si in access_size:
            si   =si.size.replace('"','')
            sizelist.append(int(si))
    typelist = []
    if access_type:
        for stype in access_type:
            stype = stype.replace('"', '')
            typelist.append(str(stype))
    output = {"size":sizelist,'stype':typelist}
    output =simplejson.dumps(output)
    return HttpResponse(output, content_type='application/json')


@csrf_exempt
def manifold_accessories(request):
    access_id = request.POST.get('selected_acc')
    access_size = AccessoriesSize.objects.filter(accessories_id=int(access_id))
    access_type = AccessoriesType.objects.filter(accessories_id=int(access_id)).values_list('type', flat=True)

    #sizedict = {}
    sizelist =  []
    if access_size:
        for si in access_size:
            print "check",si
            si   =si.size.replace('"','')
            sizelist.append(str(si))

    typelist = []
    if access_type:
        for stype in access_type:
            stype = stype.replace('"', '')
            typelist.append(str(stype))
    print "chck122",typelist
    print ">>>>>>>>>>>>",typelist
    output = {"size": sizelist, 'stype': typelist}
    output = simplejson.dumps(output)
    return HttpResponse(output, content_type='application/json')



@csrf_exempt
def header_accessories(request):
    access_id = request.POST.get('selected_acc')
    access_size = AccessoriesSize.objects.filter(accessories_id=int(access_id))
    access_type = AccessoriesType.objects.filter(accessories_id=int(access_id)).values_list('type', flat=True)

    #sizedict = {}
    sizelist =  []
    if access_size:
        for si in access_size:
            print "check",si
            si   =si.size.replace('"','')
            sizelist.append(str(si))
    typelist = []
    if access_type:
        for stype in access_type:
            stype = stype.replace('"', '')
            typelist.append(str(stype))
    print "chck122", typelist
    print ">>>>>>>>>>>>", typelist
    output = {"size": sizelist, 'stype': typelist}
    output = simplejson.dumps(output)
    return HttpResponse(output, content_type='application/json')


@csrf_exempt
def show_price(request):
    length_droppipe = request.POST.get('length')
    print "lenght???",length_droppipe
    size = request.POST.get('size')
    material = request.POST.get('material')
    piping = request.POST.get('piping')
    backend_price = Price.objects.filter(size_id=int(size),material_id=int(material),piping_id=int(piping))
    if backend_price:
        backend_price = backend_price[0].pipes_price
        print "price>>>>>",backend_price,length_droppipe
        final_price = Decimal(backend_price) * int(length_droppipe)
    return HttpResponse(final_price)


@csrf_exempt
def manifold_price(request):
    length = request.POST.get('length')
    size = request.POST.get('size')
    material = request.POST.get('material')
    piping = request.POST.get('piping')
    print "check6",length,size,material,piping
    backend_price = Price.objects.filter(size_id=int(size),material_id=int(material),piping_id=int(piping))
    print ">>>>>>>>>>>>",backend_price
    if backend_price:
        backend_price = backend_price[0].pipes_price
        final_price = Decimal(backend_price) * int(length)
    return HttpResponse(final_price)

@csrf_exempt
def header_price(request):
    length = request.POST.get('length')
    size = request.POST.get('size')
    material = request.POST.get('material')
    piping = request.POST.get('piping')
    print "check6",length,size,material,piping
    backend_price = Price.objects.filter(size_id=int(size),material_id=int(material),piping_id=int(piping))
    print ">>>>>>>>>>>>",backend_price
    if backend_price:
        backend_price = backend_price[0].pipes_price
        final_price = Decimal(backend_price) * int(length)
    return HttpResponse(final_price)



@csrf_exempt
def show_accessories_priceinfo(request):
    final_price = 0
    length_droppipe = request.POST.get('length')
    print "lenght???",length_droppipe
    size = request.POST.get('size')
    accessories = request.POST.get('accessories')
    access_type = request.POST.get('type')
    backend_price = AccessoriesPrice.objects.filter(size__size=size,name_id=int(accessories),type__type=access_type)
    if backend_price:
        backend_price = backend_price[0].accessories_price
        print "checkdwdqdqdqdw",type(backend_price)
        final_price = Decimal(backend_price) * int(length_droppipe)
    return HttpResponse(final_price)


def download_est_rpt(request,totalcost_id=''):
    result =TotalCost.objects.filter(id=int(totalcost_id))
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="estimation_report.csv"'
    writer = csv.writer(response)
    writer.writerow(["item id","Description","Total Quantity","Total Price"])
    for m in result:
        writer.writerow([int(m.id), str(m.description), int(m.quantity), int(m.total_price)
                        ])
    return response

def calculate_details(request):
    droppipe_size = request.POST.get('droppipe_size')
    droppipe_material = request.POST.get('droppipe_material')
    droppipe_Piping = request.POST.get('droppipe_Piping')
    droppipe_length = request.POST.get('droppipe_length')
    price_droppipe = request.POST.get('price_droppipe')
    desc_propipe = []
    dropipe_des1 = Material.objects.filter(id=int(droppipe_material))[0].material
    dropipe_des2 = Piping.objects.filter(id=int(droppipe_Piping))[0].piping
    dropipe_des3 = Size.objects.filter(id=int(droppipe_size))[0].size
    desc_propipe = desc_propipe.append(dropipe_des1)
    desc_propipe = desc_propipe.append(dropipe_des2)
    desc_propipe = desc_propipe.append(dropipe_des3)
    desc_propipe = ",".join(desc_propipe)

    droppipe_asses_assessories = request.POST.getlist('droppipe_accessories',None)
    droppipe_access_size = request.POST.getlist('access_size',None)
    droppipe_access_type = request.POST.getlist('access_type',None)
    droppipe_droppipe_price = request.POST.getlist('droppipe_price',0)
    droppipe_droppipe_quantity = request.POST.getlist('droppipe_quantity',0)
    droppipe_asses_assessories_list=[]
    if droppipe_asses_assessories:
        for i in droppipe_asses_assessories:
            data = Accessories.objects.filter(id=int(i))
            if data:
                droppipe_asses_assessories_list.append(data[0].name)

    all_propipe_access = zip(droppipe_asses_assessories_list,droppipe_access_size,droppipe_access_type,droppipe_droppipe_quantity,droppipe_droppipe_price)
    total_dropipe_ass_price = 0.0
    total_dropipe_ass_quantity = 0
    for i in droppipe_droppipe_price:
        total_dropipe_ass_price = Decimal(total_dropipe_ass_price) + Decimal(i)
    for i in droppipe_droppipe_quantity:
        total_dropipe_ass_quantity = int(total_dropipe_ass_quantity) + int(i)

    manifold_size = request.POST.get('manifold_size')
    manifold_material = request.POST.get('manifold_material')
    manifold_material = request.POST.get('manifold_Piping')
    manifold_length = request.POST.get('manifold_length')
    price_manifold = request.POST.get('price_manifold')
    desc_manifold = []
    manifold_des1 = Material.objects.filter(id=int(manifold_material))[0].material
    manifold_des2 = Piping.objects.filter(id=int(manifold_material))[0].piping
    manifold_des3 = Size.objects.filter(id=int(manifold_size))[0].size
    desc_manifold = desc_propipe.append(manifold_des1)
    desc_manifold = desc_propipe.append(manifold_des2)
    desc_manifold = desc_propipe.append(manifold_des3)
    desc_manifold = ",".join(desc_manifold)

    manifold_asses_assessories = request.POST.getlist('manifold_accessories',None)
    manifold_access_size = request.POST.getlist('access_manifold_size',None)
    manifold_access_type = request.POST.getlist('access_manifold_type',None)
    manifold_price = request.POST.getlist('manifold_access_price',0)
    manifold_quantity = request.POST.getlist('manifold_access_quntity',0)
    manifold_asses_assessories_list = []
    if manifold_asses_assessories:
        for i in manifold_asses_assessories:
            data = Accessories.objects.filter(id=int(i))
            if data:
                manifold_asses_assessories_list.append(data[0].name)
    all_manifold_access = zip(manifold_asses_assessories_list,manifold_access_size,manifold_access_type,manifold_price,manifold_quantity)
    total_manifold_ass_price = 0.0
    total_manifold_ass_quantity = 0
    for i in manifold_price:
        total_manifold_ass_price = Decimal(total_manifold_ass_price) + Decimal(i)
    for i in manifold_quantity:
        total_manifold_ass_quantity = int(total_manifold_ass_quantity) + int(i)

    headers_size = request.POST.get('headers_size')
    headers_material = request.POST.get('headers_material')
    headers_Piping = request.POST.get('headers_Piping')
    headers_length = request.POST.get('headers_length')
    price_header = request.POST.get('price_header')
    desc_header = []
    header_des1 = Material.objects.filter(id=int(headers_material))[0].material
    header_des2 = Piping.objects.filter(id=int(headers_Piping))[0].piping
    header_des3 = Size.objects.filter(id=int(headers_size))[0].size
    desc_header = desc_propipe.append(header_des1)
    desc_header = desc_propipe.append(header_des2)
    desc_header = desc_propipe.append(header_des3)
    desc_header = ",".join(desc_manifold)

    header_asses_assessories = request.POST.getlist('headers_accessories',None)
    header_access_size = request.POST.getlist('headers_size',None)
    header_access_type = request.POST.getlist('headers_type',None)
    header_price = request.POST.getlist('header_access_price',0)
    header_quantity = request.POST.getlist('header_access_quntity',0)
    header_asses_assessories_list = []
    if header_asses_assessories:
        for i in header_asses_assessories:
            data = Accessories.objects.filter(id=int(i))
            if data:
                header_asses_assessories_list.append(data[0].name)
    all_header_access = zip(header_asses_assessories_list,header_access_size,header_access_type,header_price,header_quantity)
    total_header_ass_price = 0.0
    total_header_ass_quantity = 0
    for i in header_price:
        total_header_ass_price = Decimal(total_header_ass_price) + Decimal(i)
    for i in header_quantity:
        total_header_ass_quantity = int(total_header_ass_quantity) + int(i)
    total_price = Decimal(price_droppipe) + Decimal(price_manifold) + Decimal(price_header) + Decimal(
        total_header_ass_price) + Decimal(total_manifold_ass_price) + Decimal(total_dropipe_ass_price)
    # description = []
    # description.append(des1)
    # description.append(des2)
    # description.append(des3)
    # final_description = ",".join(description)
    # total_price_obj = TotalCost()
    # total_price_obj.description = final_description
    # total_price_obj.unit_price = 0
    # total_price_obj.quantity = total_quantity
    # total_price_obj.total_price = total_price
    # total_price_obj.save()
    # return total_price_obj
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="estimation_report.csv"'
    writer = csv.writer(response)
    writer.writerow(["item id", "Description", "Total Quantity", "Total Price"])
    #writer.writerow([int(1), str(desc_propipe), int(droppipe_length), int(price_droppipe)])
    writer.writerow([int(2), str(desc_manifold), int(manifold_length), int(manifold_length)])
    return response